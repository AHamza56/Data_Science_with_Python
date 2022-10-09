import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.header(''' 
 **This app is developed by Mr. Ali Hamza**
Exploratory Data Analysis web app
''')

df=sns.load_dataset("iris")
st.write(df[['species', 'sepal_length', 'petal_length']].head(10))

st.bar_chart(df['sepal_length'])
st.line_chart(df['sepal_length'])

