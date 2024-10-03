import streamlit as st

st.title("Liz is pretty"), st.title("liz is pretty")
if st.button("Wathing anything"):
    image_url1 = "https://imgnews.pstatic.net/image/433/2024/09/19/0000108883_001_20240919100130136.jpg?type=w647"
    st.image(image_url1)
else:
    st.write("Goodbye")
