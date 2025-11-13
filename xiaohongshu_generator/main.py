import streamlit as st
from utils import xiaohongshu_generator

st.header('小红书AI写作助手')
with st.sidebar:
   deepseek_api_key = st.text_input('请输入deepseekAPI密钥:',type='password')
   st.markdown('[点击获取API密钥](https://platform.deepseek.com/api_keys)')
theme = st.text_input('主题')
submit = st.button('开始生成')
if submit and not deepseek_api_key:
    st.info('请输入API密钥')
    st.stop()
if submit and not theme:
    st.info('请输入主题')
    st.stop()
if submit:
    with st.spinner('AI正在创作中,请稍等...'):
        result = xiaohongshu_generator(theme = theme,deepseek_api_key = deepseek_api_key)
    st.divider()
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown('##### 小红书标题1')
        st.write(result.titles[0])
        st.markdown('##### 小红书标题2')
        st.write(result.titles[1])
        st.markdown('##### 小红书标题3')
        st.write(result.titles[2])
        st.markdown('##### 小红书标题4')
        st.write(result.titles[3])
        st.markdown('##### 小红书标题5')
        st.write(result.titles[4])
    with right_column:
        st.markdown('##### 小红书正文:')
        st.write(result.content)




