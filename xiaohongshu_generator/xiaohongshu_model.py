from pydantic import BaseModel, Field
from typing import List

class xiaohongshu(BaseModel):
    titles:List[str]=Field(description='小红书的5个标题')
    content:str=Field(description='小红书的正文')