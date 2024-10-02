import streamlit as st
import pandas as pd
from streamlit_image_coordinates import streamlit_image_coordinates

value = streamlit_image_coordinates("https://placekitten.com/200/300")

st.write(value)

st.title("Liz")
