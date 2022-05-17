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

streamlit.multiselect("Pick some fruits:",List(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
