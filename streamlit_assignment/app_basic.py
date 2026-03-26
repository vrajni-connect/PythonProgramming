#create basic streamlit app that 
#1. has a title "Welcome to Streamlit Dashboard"
#2. shows a text input box for entering your name
#3. when user clicks a button "Greet Me", it displays
# "Hello !"
# use : st.title(), st.text_input(), st.button(), st.write() functions
import streamlit as st
st.title("Welcome to Streamlit Dashboard")
name=st.text_input("Enter your name")
if st.button("Greet Me"):
    st.write(f"Hello {name}!")  