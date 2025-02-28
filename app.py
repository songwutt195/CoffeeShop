import streamlit as st
from engine import Customer, Drink, Snack, Order, Payment

free_quota = 10

americano = Drink('americano', 15)
green_tea = Drink('green tea', 20)
cookie = Snack('cookie')
cake = Snack('cake')

menu = [americano, green_tea, cookie, cake]

st.title("Test Coffe Shop")
col1, col2 = st.columns(2)

with col1:
    st.header('Customer')
    st.text_input('Customer Name:')
    st.radio('Gender:', ['Male', 'Female', 'Other'])
    st.number_input('Age:', value=20, step=1)
    st.button('Check Bill')

with col2:
    st.header('Menu')
    for product in menu:
        st.number_input(f'{product.name} - {product.price}', key=product.name, value=0, step=1)