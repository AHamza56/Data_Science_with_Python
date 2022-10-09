# Import libraries
from re import A
import streamlit as st 
import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import seaborn as sns

# Set title
st.markdown(''' 
# **Exploratory Data Analysis web app**
This app is developed by Ali Hamza called **EDA**
''')

# How to upload a file from your computer
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)""")


# ProfileReport 
if uploaded_file is not None:                # if a file is uploaded
    @st.cache                                # cache the  function # speed up the app
    def load_csv():                          # define a function
        csv = pd.read_csv(uploaded_file)     # Read the uploaded file
        return csv                           # Return the csv file
    df = load_csv()                          # Call the function
    pr = ProfileReport(df, explorative=True) # Create a profile report
    st.header('**Input DataFrame**')         # Display the input dataframe
    st.write(df)                             # Display the dataframe
    st.write('---')                          # Display a horizontal line
    st.header('**Pandas Profiling Report**')   
    st_profile_report(pr)                    # Display the profile report
else:
    st.info('Awaiting for CSV file to be uploaded.') 
    if st.button('Press to use Example Dataset'): # Use the example dataset
        # example dataset
        @st.cache 
        def load_data():
            a=pd.DataFrame(np.random.rand(100, 5), columns=['age', 'banana', 'codanics', 'duty', 'education'])
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)