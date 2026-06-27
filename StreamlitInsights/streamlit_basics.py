import streamlit as st
import pandas as pd
import numpy as np

## What is Streamlit
### Streamlit is an open-source app framework for ML and DS projects. It allows you to create beautiful web applications for your ML and DS Projects with Python scripts


## Title of the aplication

st.title("Hello Good to See You on Streamlit")

## create a simple text

st.write("This is simple text")


## create a simple Dataframe

df = pd.DataFrame(
    {
    'first column':[1,2,3,4],
    'second column':['Sai','Kiran','Ajay','Robin']
}
)


## Display the Dataframe

st.write("Here is the dataframe")

st.write(df)

## create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

st.line_chart(chart_data)


