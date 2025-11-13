from prompt_template import system_template_text,user_template_text
from langchain_core.prompts import ChatPromptTemplate
from langchain_deepseek.chat_models import ChatDeepSeek
from langchain_core.output_parsers import PydanticOutputParser
from xiaohongshu_model import xiaohongshu
import os

def xiaohongshu_generator(theme,deepseek_api_key):
    prompt=ChatPromptTemplate.from_messages([('system',system_template_text),
                                             ('user',user_template_text),])
    model = ChatDeepSeek(
        api_key = deepseek_api_key,
        model="deepseek-chat",
        temperature=0.3,
    )

    outputparser=PydanticOutputParser(pydantic_object=xiaohongshu)
    chain= prompt|model|outputparser
    result=chain.invoke({'parser_instructions':outputparser.get_format_instructions(),
                         'theme':theme})
    return result
