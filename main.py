import streamlit as st

# 页面标题
st.title("Markdown Editor")

# 自定义CSS样式
st.markdown(
    """
    <style>
    .main .block-container {
        padding-top: 2rem;
        margin: 0;
        max-width: 100%;
    }
    .stTextArea textarea {
        width: 100% !important;
        height: 700px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 初始化SessionState
if 'markdown_text' not in st.session_state:
    st.session_state.markdown_text = ""

# 使用Streamlit的列布局功能创建左右分栏，设置各占50%的宽度
col1, col2 = st.columns(2)

# 左边列：输入框，用于输入markdown文本
with col1:
    markdown_text = st.text_area("Enter your markdown text", st.session_state.markdown_text)

# 右边列：渲染markdown文本
with col2:
    st.markdown(markdown_text)

# 更新SessionState
st.session_state.markdown_text = markdown_text

