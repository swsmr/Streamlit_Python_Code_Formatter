import autopep8
from yapf.yapflib.yapf_api import FormatCode
import black

import streamlit as st

st.set_page_config(page_title="Python Code Formatter", layout="wide")
st.title('Python Code Formatter')

col1, col2 = st.columns(2)

with col1:

    st.header('Input code and formatter')
    code_in = st.text_area("Paste the Python code to be formatted here:", height=250)
    if code_in:
        formatter = st.radio("Select formatter", ['yapf', 'autopep8', 'black'])
        if formatter == 'yapf':
            style_config = st.selectbox("Select yapf style", ['pep8', 'google', 'yapf', 'facebook'], index=1)
            code_out, _ = FormatCode(code_in, style_config=style_config)
        elif formatter == 'autopep8':
            code_out = autopep8.fix_code(code_in)
        elif formatter == 'black':
            code_out = black.format_str(code_in, mode=black.FileMode())
    else:
        code_out = ''

with col2:
    st.header('Formatted code')
    st.code(code_out, language='python')
