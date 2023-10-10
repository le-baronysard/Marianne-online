import streamlit as st
import pandas as pd
from src.utils import load_data,convert_devise




if not "raw_data" in st.session_state:
    st.session_state["raw_data"] = load_data()


st.markdown("## Funding Rounds")

st.dataframe(st.session_state["raw_data"])
