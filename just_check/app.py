import streamlit as st

def student_details_form():
    st.title("Student Details Form")

    # Get student details
    name = st.text_input("Name", "")
    age = st.number_input("Age", min_value=0, max_value=150, value=0)
    grade = st.selectbox("Grade", ["Freshman", "Sophomore", "Junior", "Senior"])
    address = st.text_area("Address", "")

    # Display collected details
    st.subheader("Collected Details:")
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Grade: {grade}")
    st.write(f"Address: {address}")

    # You can add more fields as needed

if __name__ == "__main__":
    student_details_form()
