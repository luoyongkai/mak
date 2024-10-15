import streamlit as st

# 设置页面为宽屏布局，确保更大显示范围
st.set_page_config(layout="wide")

# 页面标题
st.title("Markdown Editor")

# 自定义CSS样式，强制两列各占50%的宽度
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
    /* 确保每个列的宽度为50% */
    [data-testid="column"] {
        width: 50% !important;
        flex: 0 0 50% !important;
        padding: 10px;  /* 你可以调整间距 */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 创建两列，分别用于输入和渲染markdown文本
col1, col2 = st.columns([1, 1])  # 强制两列均分

# 左边列：输入框，用于输入markdown文本
with col1:
    markdown_text = st.text_area("Enter your markdown text")

# 右边列：渲染markdown文本
with col2:
    st.markdown(markdown_text)
