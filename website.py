import streamlit as st

value = [74400, 72500, 70000, 69000, 68900, 67500, 66200, 64900, 66300, 64400, 63100, 63000, 62600, 63200, 
         62200, 64700, 64200, 61500, 61300, 60600, 61000]
st.write("삼성전자 9월 이후 주가")
st.line_chart(value)
