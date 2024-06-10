#from nbformat import write
import streamlit as st
import pandas as pd
import numpy as np
import ydata_profiling
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport

st.title("MRTC-UCRBO Data Profiling App")
st.subheader("Cette application vous aidera à faire de l'exploration de données")

# Side nav
st.sidebar.image("logo.jpg",width=None)

st.sidebar.header("User Input Features")
uploaded_file = st.sidebar.file_uploader("Upload your input Excel file", type="xlsx")
if uploaded_file is not None:
    st.markdown('---')
    input_df = pd.read_excel(uploaded_file, engine="openpyxl")

    profile = ProfileReport(input_df,title="Summary of the Data")

    st.header("Detailed Report for the Uploaded Data")
    st.write(input_df)

    st_profile_report(profile)


else:
    st.markdown('---')
    st.write("You did not upload a new file")
