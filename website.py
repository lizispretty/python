import streamlit as st
import pandas as pd
from streamlit_image_coordinates import streamlit_image_coordinates

st.title("Liz")
value = streamlit_image_coordinates("https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F433%2F2024%2F09%2F19%2F0000108883_002_20240919100130173.jpg&type=a340")

st.write(value)
