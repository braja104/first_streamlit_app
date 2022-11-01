import streamlit
streamlit.title('My Parents New Health Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('\N{pot of food}  Omega 3 and Blueberry OatMeal')
streamlit.text('\N{cherries}kale,Spinach and Rocket Smoothie')
streamlit.text('\N{egg}Boiled_Egg Half Boil')
streamlit.header('Build Your Own Fruit Smoothie')
streamlit.text('\N{grapes} Grape Juice')
streamlit.text('\N{melon} Melon')
streamlit.text('\N{peach} Peach')
streamlit.text('\N{blueberries} Blueberries')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
