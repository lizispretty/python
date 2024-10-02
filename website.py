import streamlit as st
import streamlit_image_coordinates as im

image = im("https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F109%2F2024%2F07%2F21%2F0005121079_001_20240721174820007.jpg&type=a340")
st.write(image)
st.title("Liz")
