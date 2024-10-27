import streamlit as st 

department=st.text_input(label="ENTER YOUR DEPARTMENT IN SHORT FORM AND IN LOWER CASE:")
rollno=st.text_input(label="ENTER YOUR ROLL NO:")
year=st.text_input(label="ENTER YOUR JOINING YEAR")
if st.button("click here"):
    st.write("YOUR REGISTER NUMBER:",year,department,rollno)