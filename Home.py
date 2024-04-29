import streamlit as st
import time

st.image("https://cdn.midjourney.com/11cec91f-fcdf-4f5b-a380-339a069c8c39/0_0.webp", width=700)

st.write(" Innovation en santé : levées de fonds de 500 entreprises françaises ")

st.write( "Ce site a été réalisé dans le cadre d'une thèse de sciences politiques dans le but de cartographier les entreprises innovantes en santé en France et de suivre leur levée de fonds.")
st.write(" Il est mis à jour régulièrement et les données sont accessibles en Open Source.")
st.write("Pour naviguer, utilisez les onglets ci-dessous.")

import streamlit as st

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Explore", "Historical Data", "Raw Data", "Maps", "About"])

with tab1:
    
   st.page_link("pages/01-Explore.py",label= "Explore")

with tab2:
        
    st.page_link("pages/02-Historical_data.py",label= "Historical Data")

with tab3:
    st.page_link("pages/03-Raw_data.py",label= "Raw Data")
    
with tab4:
    st.page_link("pages/04-Maps.py",label= "Maps")

with tab5 :
    st.page_link("pages/05-About.py",label= "About")
