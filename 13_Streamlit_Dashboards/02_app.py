import pandas as pd
from requests import options
import seaborn as sns
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# make containers
header=st.container()
data_set=st.container()
features=st.container()
model_training=st.container()

with header:
    st.title('Titanic dataset analysis')
    st.text("In this project we will work on the data set of the Titanic")

with data_set:
    st.header('Titanic has been drowned')
    st.text("This is a really bad news")
# import data
    df=sns.load_dataset('titanic')
    df=df.dropna()
    st.write(df.head(20))
# plot data   
    st.subheader('Bar Chart of Age')
    st.bar_chart(df['sex'].value_counts())
# other plot
    st.subheader('Bar Chart of Class')
    st.bar_chart(df['class'].value_counts())
# plot with sample
    st.bar_chart(df['age'].sample(10))


with features:
    st.header('These are our app features')
    st.text("We will work on the many features")
    st.markdown('1. **Feature 1:** This a feature 1')
    st.markdown('2. **Feature 2:** This a feature 2')
    st.markdown('3. **Feature 3:** This a feature 3')
    st.markdown('4. **Feature 4:** This a feature 4') 

with model_training:
    st.header('Model training')
    st.text("We will test our model")
# making columns
    input, display=st.columns(2)
# In first column there must be selection point
    max_depth=input.slider("How many people do you want to see?", min_value=10, max_value=100, value=20, step=10)
# n_estimators
    n_estimators=input.selectbox("How many tree do you want to make in RF?", options=[50, 100, 200, 300, 'No Limit'], index=0)
# list of features
input.write(df.columns)
# input features from user
input_features= input.text_input("Feature Name")


# machine learning model
model=RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth)
# if and else condition to justify the no limit
if n_estimators=='No Limit':
    model=RandomForestRegressor(max_depth=max_depth) 
else:
     model=RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth)

# define X and y
x=df[[input_features]]
y=df[['fare']]
model.fit(x, y)
prediction=model.predict(y)

# display matrics
display.subheader('Mean absolute error')
display.write(mean_absolute_error(y, prediction))
display.subheader('Mean squared error')
display.write(mean_squared_error(y, prediction))
display.subheader('r2 score')
display.write(r2_score(y, prediction))