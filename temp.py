import streamlit as st
from PIL import Image
import pandas as pd


st.title("WELLCOME TO RKVV MARKS ENTRY PORTAL")
image = image = Image.open('logo.jpg')
st.image(image, caption='Sunrise by the mountains')
name = st.text_input("Enter Your Name")
fname= st.text_input("Enter Your fathers name")
adr = st.text_area("Enter Your Address")
classdata = st.selectbox("Select Your Class:",(1,2,3,4,5,6,7,8,9,10))
button = st.button("Submit")
if button :
    st.markdown(f"""
               Name : {name} 
               Father name : {fname}
               Class : {classdata}
               Address : {adr}

                """)
