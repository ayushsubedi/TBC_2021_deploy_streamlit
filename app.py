import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.image('https://jcss-cdn.kantipurdaily.com/kantipurdaily/images/logo.png')
st.sidebar.title ('Kantipur app')
st.sidebar.subheader('(demo) For the British College (MSCIT DS)')

st.title('Kantipur app')
st.subheader('something')

# Input
user_input = st.text_input("caret (supports ints only)", 0.5)
st.subheader(user_input)

option = st.selectbox(
    'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

# Output
st.title('price is 500')