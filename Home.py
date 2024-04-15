import streamlit as st
from Hospital import show_hospital_page
from app2 import show_crime_page

def show_home():
    st.title("Welcome to the Safety & Health Locator App")
    st.write("Please select one of the options below to continue:")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Hospital Finder"):
            show_hospital_page()
    with col2:
        if st.button("Crime Spot Locator"):
            show_crime_page()

if __name__ == "__main__":
    show_home()
