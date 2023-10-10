import streamlit as st
import time

st.markdown("<h1 style='text-align: center; color: blue;'>Hello Marianne</h1>", unsafe_allow_html=True)

st.balloons()

st.write("")
st.write("Work in progress")
my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(1)
    my_bar.progress(percent_complete + 1)
