import streamlit as st
import pandas as pd

st.title("Data Upload Demo")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
# File uploader widget
uploaded_file = st.file_uploader("Upload your data file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Read the file depending on type
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    st.write("Here’s a preview of your data:")
    st.dataframe(df.head())
