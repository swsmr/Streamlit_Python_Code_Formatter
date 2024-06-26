import subprocess
import tempfile

import autopep8
from yapf.yapflib.yapf_api import FormatCode
import black

import streamlit as st

st.set_page_config(page_title="Python Code Formatter", layout="wide", page_icon=':snake:')
st.title('Python Code Formatter')

with st.sidebar:
    st.header('Settings')
    formatter = st.radio("Select formatter", ['yapf', 'autopep8', 'black'])
    if formatter == 'yapf':
        style_config = st.selectbox("Select yapf style", ['pep8', 'google', 'yapf', 'facebook'], index=1)

st.header('Input code')
code_in = st.text_area("Paste the Python code to be formatted here:", 
                       height=None, # 150
                       label_visibility="collapsed", # "visible"
                      )
if code_in:
    if formatter == 'yapf':
        code_out, _ = FormatCode(code_in, style_config=style_config)
    elif formatter == 'autopep8':
        code_out = autopep8.fix_code(code_in)
    elif formatter == 'black':
        # code_out = black.format_str(code_in, mode=black.FileMode()) # mode=black.Mode()
        # code_out = black.format_file_contents(code_in, fast=False, mode=black.Mode()) # target_versions={black.TargetVersion.PY311}, # , line_length=120 # mode=black.FileMode(),
        # code_out = subprocess.run(["black", "-c", code_in], capture_output=True, text=True).stdout
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as fp:
            fp.write(code_in)
            fp.close()
            # the file is closed, but not removed

            # Run black
            subprocess.run(["black", fp.name])
                           
            # open the file again by using its name
            with open(fp.name, mode='r') as f:                
                code_out = f.read()

    st.header('Formatted code')
    st.code(code_out, language='python', line_numbers=st.sidebar.toggle("Display line numbers?", value=False))
