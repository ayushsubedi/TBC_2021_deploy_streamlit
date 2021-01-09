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
user_input_caret = st.text_input("supports ints only", 0.23, key='caret')

st.subheader('Input cut')
option_cut = st.selectbox(
    'Whats the diamond cut?',
     ('Email', 'Home phone', 'Mobile phone'), key='cut')

st.subheader('Input color')
option_color = st.selectbox(
    'Whats the diamond cut?',
     ('Email', 'Home phone', 'Mobile phone'), key='color')

st.subheader('Input clarity')
option_clarity = st.selectbox(
    'Whats the diamond cut?',
     ('Email', 'Home phone', 'Mobile phone'), key='clarity')

st.subheader('Input x')
user_input_x = st.text_input("supports ints only", 3.9, key ='x')

st.subheader('Input y')
user_input_y = st.text_input("supports ints only", 3.9, key='y')

st.subheader('Input z')
user_input_z = st.text_input("supports ints only", 2.4, key = 'z')


st.subheader('Your input dataframe')
df = pd.DataFrame([{'carat': user_input_caret, 'cut':option_cut, 'color':option_color, 'clarity':option_clarity, 'x':user_input_x, 'y':user_input_y, 'z':user_input_z}])
st.table(df)

model = pickle.load(open('static/saved_models/randomforestregressor.pkl', 'rb'))
cut_le = pickle.load(open('static/saved_models/cut_le.pkl', 'rb'))
color_le= pickle.load(open('static/saved_models/color_le.pkl', 'rb'))
clarity_le = pickle.load(open('static/saved_models/clarity_le.pkl', 'rb'))
df['cut'] = cut_le.transform(df['cut'])
df['color'] = color_le.transform(df['color'])
df['clarity'] = clarity_le.transform(df['clarity'])
result = model.predict(df)[0]


# Output
st.title('Thanks for using our model to predict price of diamond. The prediction is: '+result)