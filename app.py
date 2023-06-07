import streamlit as st
import pandas as pd
import numpy as np

st.title('Simple Data Exploratory Analysis')
uploaded_file = st.file_uploader(label = "To get started, please upload your data using the uploader below. Please ensure that the file you have chosen is a **.csv** file!", type = "csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    st.write(f"The number of rows in the dataframe is: {len(df.index)} rows.")
    st.write(f"The number of columns in the dataframe is: {len(df.columns)} columns.")
    st.write(f"The number of categorical variables is:.")
    

#st.sidebar.title('title of sidebar')
#st.sidebar.markdown('markdown **text** in the *sidebar*')

#agree = st.checkbox('I agree')

#if agree:
#    st.write('Great!')
#    st.markdown("this is markdown **text**")

#agree_sidebar = st.sidebar.checkbox('side bar checkbox')

#if agree_sidebar:
#    st.sidebar.write('side bar checked')