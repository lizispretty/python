import streamlit as st
import streamlit_image_coordinates as im

image = im("https://search.naver.com/search.naver?ssc=tab.image.all&where=image&sm=tab_jum&query=%EB%A6%AC%EC%A6%88#imgId=image_sas%3Anews_6fe6169a625961c3bf29ef27e9c2f429")
st.write(image)
st.title("Liz")
