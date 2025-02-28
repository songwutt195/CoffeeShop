import streamlit as st
from datetime import datetime
from engine import Customer, Drink, Snack, Order, Payment

st.session_state.menber_id = ''
st.session_state.menber_name = ''
st.session_state.menber_gender = 'other'
st.session_state.menber_age = 20

free_quota = 10

gender_choice = ['Male', 'Female', 'other']

americano = Drink('americano', 15)
green_tea = Drink('green tea', 20)
cookie = Snack('cookie')
cake = Snack('cake')

menu = [americano, green_tea, cookie, cake]

customer = Customer(st.session_state.menber_gender, st.session_state.menber_age)
order = Order(datetime.now(), customer)
pos = Payment()

st.markdown('<h1 style="text-align: center">Test Coffe Shop</h1>', unsafe_allow_html=True)
st.markdown(f'<h5 style="text-align: right">Today Free Quota: {free_quota}</h5>', unsafe_allow_html=True)

customer_side, order_side = st.columns(2)

with customer_side:
    st.header('Customer')
    cus_id = st.text_input('Customer ID:', value=st.session_state.menber_id)
    cus_name = st.text_input('Customer Name:', value=st.session_state.menber_name)
    col1, col2 = st.columns([1,3])
    with col1:
        st.button('Identify')
    with col2:
        cus_gender = st.pills('Gender:', gender_choice, default=st.session_state.menber_gender)
    cus_age = st.number_input('Age:', value=st.session_state.menber_age, step=1)
    
    col1, col2 = st.columns(2)
    with col1:
        st.button('New Customer', use_container_width=True)
    with col2:
        st.button('Discount', use_container_width=True)

with order_side:
    st.header('Menu')
    for product in menu:
        if product.type == 'main':
            menu_label = f'{product.name} - {product.price}'
        elif product.type == 'free':
            menu_label = f'{product.name} - free'
        st.number_input(menu_label, key=product.name, value=0, step=1)
    
    col1, col2 = st.columns(2)
    with col1:
        st.button('Order', use_container_width=True)
    with col2:
        st.button('Check Bill', use_container_width=True)