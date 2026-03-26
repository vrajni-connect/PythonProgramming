"""
create a small dashboard with title + description 'simple sales dashboard'
add selectbox with months 
months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
add a disvtonary of monthly sales
sales = {
    "January": 1000,    
    "February": 1500,
    "March": 1200,
    "April": 1800,
    }

display selected months sales using st.metric() or st.write() function
display a bar chart using st.bar_chart(list(sales.values())).

"""

import streamlit as st

st.title("Simple Sales Dashboard")
st.write("This dashboard shows the monthly sales data.")
months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
sales = {   
    "January": 1000,
    "February": 1500,
    "March": 1200,
    "April": 1800,
    }

selected_month = st.selectbox("Select a month", months)
st.metric(label=f"Sales for {selected_month}", value=sales.get(selected_month, 0))
st.bar_chart(list(sales.values()))
    