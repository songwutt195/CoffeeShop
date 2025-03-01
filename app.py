import streamlit as st
import pandas as pd
from datetime import datetime
from engine import Customer, Drink, Snack, Order, Payment, MemberCustomer

if 'customer_id' not in st.session_state:
    st.session_state.customer_id = ''
if 'customer_name' not in st.session_state:
    st.session_state.customer_name = ''
if 'customer_gender' not in st.session_state:
    st.session_state.customer_gender = 'other'
if 'customer_age' not in st.session_state:
    st.session_state.customer_age = 20

free_quota = 10

gender_choice = ['male', 'female', 'other']

americano = Drink('americano', 15)
green_tea = Drink('green tea', 20)
cookie = Snack('cookie')
cake = Snack('cake')

menu = [americano, green_tea, cookie, cake]

# customer = Customer('other', 20)
# order = Order(datetime.now(), customer)

def system_reset():
    customer = Customer('other', 20)
    order = Order(datetime.now(), customer)
    for product in menu:
        st.session_state[product.name] = 0

pos = Payment()
# system_reset()

df_member = pd.read_csv('member.csv')

def customer_identify(search_id = '', search_name =''):
    if search_id == '':
        search_id = 0
    elif search_id.isnumeric():
        search_id = int(search_id)

    if search_id in df_member['id'].values:
        key = 'id'
        search_key = search_id
    elif search_name in df_member['name'].values:
        key = 'name'
        search_key = search_name
    else:
        key = None

    if key is None:
        st.toast('Member Not Found!')
        return Customer(st.session_state.customer_gender, st.session_state.customer_age)
    else:
        st.toast('Member is Found!')
        member_dict = df_member[df_member[key] == search_key].to_dict('records')[0]
        st.session_state.customer_id = member_dict['id']
        st.session_state.customer_name = member_dict['name']
        st.session_state.customer_gender = member_dict['gender']
        st.session_state.customer_age = member_dict['age']
        return MemberCustomer(st.session_state.customer_id,
                              st.session_state.customer_name,
                              st.session_state.customer_gender,
                              st.session_state.customer_age)

st.markdown('<h1 style="text-align: center">Test Coffe Shop</h1>', unsafe_allow_html=True)
st.markdown(f'<h5 style="text-align: right">Today Free Quota: {free_quota}</h5>', unsafe_allow_html=True)

customer_side, order_side = st.columns(2)

with customer_side:
    st.header('Customer')
    col1, col2 = st.columns([1,3])
    with col1:
        if st.button('Identify'):
            customer = customer_identify(st.session_state.cus_id, st.session_state.cus_name)
    with col2:
        st.text_input('id :', value=st.session_state.customer_id, key='cus_id')
    st.text_input('name :', value=st.session_state.customer_name, key='cus_name')
    st.pills('Gender:', gender_choice, default=st.session_state.customer_gender, key='cus_gender')
    st.number_input('Age:', value=st.session_state.customer_age, min_value=0, step=1, key='cus_age')

with order_side:
    st.header('Menu')
    for product in menu:
        if product.type == 'main':
            menu_label = f'{product.name} - {product.price}'
        elif product.type == 'free':
            menu_label = f'{product.name} - free'
        st.number_input(menu_label, key=product.name, min_value=0, step=1)
    
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button('New Customer', use_container_width=True):
        customer = Customer(st.session_state.cus_gender, st.session_state.cus_age)
        st.toast('Success set Customer!')
with col2:
    if st.button('Order', use_container_width=True):
        order = Order(datetime.now(), customer)
        for product in menu:
            for i in range(st.session_state[product.name]):
                order.add_item(product)
        st.toast(f'Success add {len(order.items)} item(s)!')
with col3:
    if st.button('Discount', use_container_width=True):
        customer.discount(order)
        st.toast('Success discount order!')
with col4:
    if st.button('Check Bill', use_container_width=True):
        txt = pos.check_bill(order)
        st.toast(txt)
        # system_reset()