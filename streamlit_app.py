import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥤🥬 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🍊 Create Your Own Smoothie 🥝🍑')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Strawberries'])
streamlit.dataframe(my_fruit_list)
