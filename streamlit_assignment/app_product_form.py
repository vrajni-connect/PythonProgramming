"""
create a simple form UI 
1. streamlit sidebar to enter 
product name, category(selectbox with 3-5 options), price
2. when user clicks add product, show: user components - st.sidebar.textinput, st.sidebar.selectbox,
st.sidebar.number_input
st.sidebar.button
"""
import streamlit as st
st.sidebar.title("Add a Product")
product_name=st.sidebar.text_input("Enter product name")
category=st.sidebar.selectbox("Select category", ["Electronics", "Clothing", "  Books", "Home & Kitchen"])
price=st.sidebar.number_input("Enter product price", min_value=0.0, step=0.01)
if st.sidebar.button("Add Product"):
    st.success(f"Product '{product_name}' added successfully!")
    st.write(f"Product Name: {product_name}")
    st.write(f"Category: {category}")
    st.write(f"Price: ${price}")

    