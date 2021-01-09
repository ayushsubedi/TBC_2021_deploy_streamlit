import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.image('https://images.vexels.com/media/users/3/203315/isolated/preview/7d99e56b1a5aae22e54d91bc1db965f6-orange-diamond-flat-by-vexels.png', width=300)
st.sidebar.title ('Diamond Price Prediction')
st.sidebar.subheader('For MSCIT DS Class')
st.sidebar.info('Deploying a machine learning model, known as model deployment, simply means to integrate a machine learning model and integrate it into an existing production environment (1) where it can take in an input and return an output.')


st.title('Input your diamond features')


# Input
st.subheader('Input caret')
user_input = st.text_input("supports ints only", 0.23, key='caret')

st.subheader('Input cut')
option = st.selectbox(
    'Whats the diamond cut?',
     ('Email', 'Home phone', 'Mobile phone'), key='cut')

st.subheader('Input color')
option = st.selectbox(
    'Whats the diamond cut?',
     ('Email', 'Home phone', 'Mobile phone'), key='color')

st.subheader('Input clarity')
option = st.selectbox(
    'Whats the diamond cut?',
     ('Email', 'Home phone', 'Mobile phone'), key='clarity')

st.subheader('Input x')
user_input = st.text_input("supports ints only", 3.9, key ='x')

st.subheader('Input y')
user_input = st.text_input("supports ints only", 3.9, key='y')

st.subheader('Input z')
user_input = st.text_input("supports ints only", 2.4, key = 'z')


# Output
st.title('Thanks for using our model to predict price of diamond. The prediction is 500.')