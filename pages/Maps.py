import pandas as pd
import streamlit as st

loc = pd.read_csv("data/location.csv")

st.markdown("Bonjour")
st.write(loc.isna().sum())