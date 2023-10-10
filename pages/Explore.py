import streamlit as st
import pandas as pd
from src.utils import load_data
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


if not "raw_data" in st.session_state:
    st.session_state["raw_data"] = load_data()

# str = st.text_input("Enter the name of the company you want to explore:")

def lookup(str):
    if str == "" : return st.warning("Please enter a company name")
    st.session_state["current_company"] = st.session_state.raw_data[st.session_state.raw_data["Organization Name"]==str].reset_index(drop=True)
    st.write(st.session_state["current_company"])
    st.session_state["Company name"] = str
    st.session_state["Location"] = st.session_state["current_company"]["Organization Location"].iloc[0]
    url = st.session_state["current_company"].loc[0,"Organization Website"]
    st.write(f'## [{st.session_state["Company name"]}](%s)' % url)
    st.write(f'Category : {st.session_state["current_company"].loc[0,"Organization Industries"]}')
    st.write(f'Location : {st.session_state["Location"]}')
    st.write(f'{st.session_state["current_company"].loc[0,"Organization Description"]}')
    draw_box()


def draw_box():
    data = st.session_state["current_company"].sort_values(by="Type", ascending=True)
    data.rename(columns={"Type":"Type of funding"}, inplace=True)
    plot = sns.barplot(x="Date",y="Raised (million €)",data=data,hue = "Type of funding",palette="viridis",dodge=False)
    # Make most of the ticklabels empty so the labels don't get too crowded
    ticklabels = [item.strftime('%b %d\n%Y') for item in data.Date]
    plot.xaxis.set_major_formatter(ticker.FixedFormatter(ticklabels))
    st.pyplot(plot.get_figure())

str = st.selectbox("Select a company",options=st.session_state.raw_data["Organization Name"].unique())
if st.button("Explore",on_click=lookup(str)):
    st.write("ok")
else :
    st.write("Sad")
