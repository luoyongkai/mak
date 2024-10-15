import streamlit as st

# 页面标题
st.title("Markdown Editor")

# 自定义CSS样式，强制列宽为50%
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
        height: 700px !important;  /* 手动调整高度 */
    }
    /* 确保列宽为50% */
    [data-testid="column"] {
        width: calc(50% - 1rem) !important;
        flex: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 使用Streamlit的列布局功能创建左右分栏，设置各占50%的宽度
col1, col2 = st.columns(2)

# 左边列：输入框，用于输入markdown文本
with col1:
    markdown_text = st.text_area("Enter your markdown text")

# 右边列：渲染markdown文本
with col2:
    st.markdown(markdown_text)
