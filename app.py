import streamlit as st


st.title('Python debugging in Windows')


error_text = st.text_area('Enter your error here', height=200)

if error_text:
    st.write(f"You entered: {error_text}")

    st.header("Only known fix: Switch to Mac or Linux")