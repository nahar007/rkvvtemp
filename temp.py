import streamlit as st
from PIL import Image
import pandas as pd
import os

st.title("WELCOME TO RKVV MARKS ENTRY PORTAL")
image = Image.open('logo.jpg')
st.image(image, caption='Sunrise by the mountains')

# Load existing data from the Excel file if it exists, otherwise create a new DataFrame
if os.path.isfile('user_data.xlsx'):
    existing_data = pd.read_excel('user_data.xlsx')
else:
    existing_data = pd.DataFrame()

name = st.text_input("Enter Your Name")
fname = st.text_input("Enter Your Father's Name")
adr = st.text_area("Enter Your Address")
classdata = st.selectbox("Select Your Class:", (1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
button = st.button("Submit")

if button:
    # Generate a serial number based on the number of existing rows
    serial_number = len(existing_data) + 1

    # Create a DataFrame with the new user's input data
    new_data = pd.DataFrame({'Serial Number': [serial_number],
                             'Name': [name],
                             'Father Name': [fname],
                             'Address': [adr],
                             'Class': [classdata]})

    # Append the new data to the existing data (if any)
    updated_data = pd.concat([existing_data, new_data], ignore_index=True)

    # Save the updated data to the Excel file
    updated_data.to_excel('user_data.xlsx', index=False)

    # Display the submitted data
    st.markdown(f"""
           Serial Number : {serial_number}
           Name : {name} 
           Father Name : {fname}
           Class : {classdata}
           Address : {adr}
    """)
    st.success("Data saved to user_data.xlsx")
