import streamlit as st
from PIL import Image

img = Image.open("C:/Users/PC/Pictures/리즈/liz.jpg")
st.image(img)
