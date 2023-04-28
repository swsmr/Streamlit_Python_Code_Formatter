import autopep8
from yapf.yapflib.yapf_api import FormatCode
import black

import streamlit as st

st.set_page_config(page_title="Online Python code auto-formatter", layout="wide")
st.title('Online Python code auto-formatter')

col1, col2 = st.columns(2)

with col1.form("my_form"):
   
   code_in = st.text_area("Input code")
   
   formatter = st.radio("Formatter", ['yapf', 'autopep8', 'black'])
   
   if formatter == 'yapf':
       style_config = st.selectbox("yapf style", ['pep8', 'google', 'yapf', 'facebook'], index=1)

   # Every form must have a submit button.
   submitted = st.form_submit_button("Format code")
   if submitted:
       
       if formatter == 'yapf':
           code_out, changed = FormatCode(code_in, style_config=style_config)
       elif formatter == 'autopep8':
           code_out = autopep8.fix_code(code_in)
       elif formatter == 'black':
           code_out = black.format_str(code_in, mode=black.FileMode())
       
       col2.code(code_out, language='python')
