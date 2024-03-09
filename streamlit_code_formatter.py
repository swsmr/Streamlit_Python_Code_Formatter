import autopep8
from yapf.yapflib.yapf_api import FormatCode
import black

import streamlit as st

st.set_page_config(page_title="Python Code Formatter", layout="wide")
st.title('Python Code Formatter')

with st.sidebar:
    formatter = st.radio("Select formatter", ['yapf', 'autopep8', 'black'])
    if formatter == 'yapf':
        style_config = st.selectbox("Select yapf style", ['pep8', 'google', 'yapf', 'facebook'], index=1)

st.header('Input code and formatter')
code_in = st.text_area("Paste the Python code to be formatted here:", height=150, label_visibility="collapsed")
if code_in:
    if formatter == 'yapf':
        code_out, _ = FormatCode(code_in, style_config=style_config)
    elif formatter == 'autopep8':
        code_out = autopep8.fix_code(code_in)
    elif formatter == 'black':
        code_out = black.format_str(code_in, mode=black.FileMode())

    st.header('Formatted code')
    st.code(code_out, language='python', line_numbers=True)
