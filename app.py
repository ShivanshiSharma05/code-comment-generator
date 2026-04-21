import streamlit as st
from model import generate_comments_inline

# -------------------------------
# 🔹 PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Code Comment Generator",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -------------------------------
# 🔹 CUSTOM CSS (PROFESSIONAL LOOK)
# -------------------------------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}

.stApp {
    background-color: #0f172a;
    color: #ffffff;
}

textarea {
    background-color: #111827 !important;
    color: #ffffff !important;
    border-radius: 10px !important;
}

.stButton>button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: bold;
}

.stButton>button:hover {
    background-color: #1d4ed8;
}

.code-box {
    background-color: #111827;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# 🔹 HEADER
# -------------------------------
st.markdown("<h1 style='text-align: center;'>💻 Code Comment Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af;'>Automatically generate meaningful comments for your Python code</p>", unsafe_allow_html=True)

st.markdown("---")

# -------------------------------
# 🔹 INPUT SECTION
# -------------------------------
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Input Code")
    code_input = st.text_area("Enter your code here:", height=300)

with col2:
    st.subheader("📌 Output")

    if "output" not in st.session_state:
        st.session_state.output = ""

    if st.button("🚀 Generate Comments"):
        if code_input.strip() == "":
            st.warning("Please enter some code.")
        else:
            st.session_state.output = generate_comments_inline(code_input)

    if st.session_state.output:
        st.code(st.session_state.output, language="python")

# -------------------------------
# 🔹 FOOTER
# -------------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>Built using Python & Streamlit</p>",
    unsafe_allow_html=True
)