import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Simple Data Exploratory Analysis')
uploaded_file = st.file_uploader(label = "To get started, please upload your data using the uploader below. Please ensure that the file you have chosen is a **.csv** file!", type = "csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    st.write(f"The number of rows in the dataframe is: {len(df.index)} rows.")
    st.write(f"The number of columns in the dataframe is: {len(df.columns)} columns.")
    st.write(f"The number of numerical variables is: {len(df.select_dtypes(include = [np.number]).columns)}.")
    st.write(f"The number of categorical variables is: {len(df.select_dtypes(include = [np.object_]).columns)}.")
    st.write(f"The number of bool variables is: {len(df.select_dtypes(include = [np.bool_]).columns)}.")
    
    st.write("##")
    
    choice = st.selectbox("Which column would you like more information about?", df.columns)
    st.write("You selected:", choice)
    if np.issubdtype(df[choice].dtype, np.number):
        five_num_sum = df[choice].describe()
        st.write(five_num_sum)
        fig = plt.figure(figsize = (10, 4))
        sns.distplot(df[choice], kde = True, hist = True, color = "darkblue")
        plt.xlabel(choice)
        plt.ylabel("Frequency")
        plt.title(f"Distribution Plot of {choice}")
        st.pyplot(fig)
    if np.issubdtype(df[choice].dtype, np.object_):
        counts = df[choice].value_counts(normalize = True)
        prop = pd.DataFrame({"Value": counts.index, "Proportion": counts.values})
        st.write(prop)