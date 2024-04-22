import streamlit as st
import pandas as pd
from src.utils import load_data,convert_devise

if not "raw_data" in st.session_state:
    st.session_state["raw_data"] = load_data()
    # Group by city ans sum money raised
    city = st.session_state["raw_data"].groupby("Organization Location").agg({"Raised (million €)":"sum"})
    city.sort_values(by="Raised (million €)",ascending=False,inplace=True)
    #city["Raised (million €)"] = city["Raised (million €)"].apply(lambda x: convert_devise(x))
    st.write("### Total money raised by city")
    st.write(city  )
    st.dataframe(city)  


st.markdown("## Funding Rounds")

st.dataframe(st.session_state["raw_data"])
