import streamlit as st

st.title("Square Calculator")

num = st.text_input("Enter a number:")

if st.button("Calculate Square"):
    try:
        number = float(num)
        square = number ** 2
        st.success(f"The square of {number} is {square}")
    except ValueError:
        st.error("Invalid input! Please enter a number.")
