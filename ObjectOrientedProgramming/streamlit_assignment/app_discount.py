"""
Build a simple calculator app using Streamlit that allows users to perform basic arithmetic operations (addition, subtraction, multiplication, division) on two numbers. The app should have input fields for the two numbers and a dropdown menu to select the operation. Display the result of the calculation when the user clicks a button.
1. takes product price  as Number input from user
2. takes discount percentage as Number input from user
3. on button click calculate discounted price
4. shows result using st.success() function
example
Original price: 1000
Discount percentage: 10
Final price after discount: 900
show comparison in small table 
Before | After
use st.table() function to show the list of lists
"""
import streamlit as st
price = st.number_input("Enter product price", min_value=0.0, step=0.01)
discount = st.number_input("Enter discount percentage", min_value=0.0, max_value=100.0, step=0.1)
if st.button("Calculate Discounted Price"):
    discounted_price = price - (price * discount / 100)
    st.success(f"Final price after discount: {discounted_price}")
    comparison_data = [["Before", "After"], [price, discounted_price]]
    st.table(comparison_data)