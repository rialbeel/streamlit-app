import streamlit as st

st.title('Simple Data Exploratory Analysis')
st.markdown('To get started, please upload a .csv file of your choice using the button below')
st.file_uploader(label = "Upload File")

#st.sidebar.title('title of sidebar')
#st.sidebar.markdown('markdown **text** in the *sidebar*')

#agree = st.checkbox('I agree')

#if agree:
#    st.write('Great!')
#    st.markdown("this is markdown **text**")

#agree_sidebar = st.sidebar.checkbox('side bar checkbox')

#if agree_sidebar:
#    st.sidebar.write('side bar checked')