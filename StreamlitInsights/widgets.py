import streamlit as st
import pandas as pd

st.title('Widgets and Few other interactions are here')

# input creation
name = st.text_input('Enter your name:')

if name:
    st.write(f'Hello, {name}!')

# slider creation

slider_sample = st.slider('Select your age:',1,100,18)

st.write(f'Your age is: {slider_sample}')

# data frame creation

df = pd.DataFrame(
    {
    'first column':[1,2,3,4],
    'second column':['Sai','Kiran','Ajay','Robin']
}
)


## Display the Dataframe

st.write("Here is the dataframe")

st.write(df)

# Choices creation

choice_sample = st.selectbox('Select your Course:',['Python','Java','C++'])

st.write(f'Your course: {choice_sample}')

# file upload example

upload_files = st.file_uploader('Choose your file','csv')

if upload_files is not None:
    df = pd.read_csv(upload_files)
    st.write(df)
