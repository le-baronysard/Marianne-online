import pandas as pd
import streamlit as st
import pandas as pd
import numpy as np
from src.utils import load_data,convert_devise


if not "map" in st.session_state:
    loc = pd.read_csv("data/location.csv").dropna()
    st.session_state["map"] = loc.groupby("Organization Location").agg({'lat':"mean",'lon':"mean"}).reset_index()
    count = loc.groupby("Organization Location").count().iloc[:,0]
    st.session_state["map"]["count"] = count.values * 100
    
if not "raw_data" in st.session_state:
    st.session_state["raw_data"] = load_data()

if not "city" in st.session_state:
    # Group by city ans sum money raised
    st.session_state["city"] = st.session_state["raw_data"].groupby("Organization Location").agg({"Raised (million €)":"sum"})
    st.session_state["city"].sort_values(by="Raised (million €)",ascending=False,inplace=True)
    st.session_state["city"]["Raised (million €)"] = st.session_state["city"]["Raised (million €)"].apply(lambda x: round(x))


st.markdown("### French Health Start-Up companies distribution in France : ")

st.map(st.session_state["map"],latitude="lat",longitude="lon",size="count",)


st.markdown("### Top 10 cities with the most HealthTech companies : ")
# Bar plot of the top 10 cities with the most HealthTech companies
top_10 = st.session_state["map"].set_index("Organization Location").sort_values(by="count",ascending=False).head(10) 
st.bar_chart(top_10["count"]/100)

st.markdown("### Top 10 cities by money raised (milion €): ")
# Bar plot of the top 10 cities by money raised
st.bar_chart(st.session_state["city"]["Raised (million €)"].head(10))
