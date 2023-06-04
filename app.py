import streamlit as st
import pandas as pd
import numpy as np

st.title('Simple Data Exploratory Analysis')
uploaded_file = st.file_uploader(label = "To get started, please upload your data using the uploader below. Please ensure that the file you have chosen is a **.csv** file!", type = "csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(f"The number of rows in the dataframe is: {df.shape[0]}.")
    st.write(f"The number of rows in the dataframe is: {df.shape[1]}")
    st.write(f"The number of numerical variables is: {len(df.select_dtypes("number").column)}")
    st.write(f"The number of bool variables is: {len(df.select_dtypes("bool").column)}")
    st.write(f"The number of categorical variables is: {len(df.select_dtypes("object").column)}")

#st.sidebar.title('title of sidebar')
#st.sidebar.markdown('markdown **text** in the *sidebar*')

#agree = st.checkbox('I agree')

#if agree:
#    st.write('Great!')
#    st.markdown("this is markdown **text**")

#agree_sidebar = st.sidebar.checkbox('side bar checkbox')

#if agree_sidebar:
#    st.sidebar.write('side bar checked')