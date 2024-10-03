import streamlit as st

from PIL import Image

img = Image.open('C:/Users/PC/Pictures/liz/liz.jpg')
st.image(img)
