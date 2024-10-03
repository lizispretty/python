import streamlit as st
from PIL import Image

img = Image.open('liz/liz.jpg')
st.image(img)
