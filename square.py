import streamlit as st

st.title("Square Calculator")
st.markdown("Ask the user to input a number and print its square.")
st.markdown("- Use a try-except block to handle non-numeric input.")
st.markdown("- If the input is invalid, print 'Invalid input! Please enter a number.'")

st.markdown("---")

num = st.text_input("Enter a number:")

if st.button("Calculate Square"):
    try:
        number = float(num)
        square = number ** 2
        st.success(f"The square of {number} is {square}")
    except ValueError:
        st.error("Invalid input! Please enter a number.")
