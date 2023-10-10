import streamlit as st
from src.utils import load_data
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

st.title("Historical Data")

if not "raw_data" in st.session_state:
    st.session_state["raw_data"] = load_data()


option = st.selectbox(label="Select a vizualisation",options = ["Funding over time","Funding by type","Organization by location","Funding by Sector"])

match option:
    case "Funding over time":
        temp = st.session_state["raw_data"].copy()
        temp.set_index("Date", inplace=True)
        temp = temp.loc[:,"Raised (million €)"]
        window = st.selectbox(label="Select a window",options = ["Year","Month","Week"])

        #st.write(temp)
        match window:
            case "Year":
                #st.line_chart(temp.loc[:,"Raised (million €)"].groupby(by=temp.Date.dt.year).sum())
                st.line_chart(temp.resample("Y").sum())

            case "Month":
                st.line_chart(temp.resample("M").sum())
            case "Week":
                st.line_chart(temp.resample("W").sum())

    case ("Funding by type"):
        year = st.selectbox(label="Select a year",options = ["All"]+list(st.session_state["raw_data"].Date.dt.year.unique()))

        temp = st.session_state["raw_data"].copy()
        temp  = temp[temp.Type.str.contains("Series|Venture|Seed")]
        temp.rename(columns={"Type":"Type of funding"}, inplace=True)
        if year != "All":
            temp=temp[temp.Date.dt.year==year]
            st.write(str(year),type(year))
        plot = sns.barplot(x="Type of funding",y="Raised (million €)",data=temp)
        plot.set_xticklabels(plot.get_xticklabels(), rotation=45, horizontalalignment='right')
        plot.set_title(f'Funding by type {"by all time" if year=="All" else "in "+str(year)}')
        st.pyplot(plot.get_figure())

    case ("Organization by location"):
        temp = st.session_state["raw_data"].copy()
        temp = temp.loc[:,["Organization Name","Organization Location"]]
        temp["City"] = temp["Organization Location"].str.split(",",expand=True)[0]
        temp = temp.groupby(by="City").count().iloc[:,0].rename({"Organization Name":"Count"},axis=0)
        st.write(temp)

    case("Funding by Sector"):
        temp = st.session_state["raw_data"].copy()
        year = st.selectbox(label="Select a year",options = ["All"]+sorted(list(st.session_state["raw_data"].Date.dt.year.unique()),reverse=True))
        if year != "All":
            temp=temp[temp.Date.dt.year==year]
        top = st.select_slider(label="Select the number of bins",options = [5,10,15,20,25,30,35,40,45,50])
        temp.groupby(by="Organization Industries").sum().sort_values(by="Raised (million €)",ascending=False)
        temp  =(temp.groupby(["Organization Industries",pd.cut(temp["Raised (million €)"],bins=[0,1,10,100,100_000])]).count().iloc[:,0].rename({"Organization Name":"Count"},axis=0))
        temp = temp.unstack().reset_index()
        temp.columns = ["Organisation Industries","<1M","1-10M","10-100M",">100M"]
        temp["tot"]=temp.sum(axis=1)
        temp.sort_values(by="tot",ascending=False,inplace=True)
        temp = temp.head(top)
        fig, ax = plt.subplots()
        ax.bar(x=temp["Organisation Industries"],height=temp["<1M"])
        ax.set_xticklabels(temp["Organisation Industries"], rotation=45, horizontalalignment='right')
        ax.bar(x=temp["Organisation Industries"],height=temp["1-10M"],bottom=temp["<1M"])
        ax.bar(x=temp["Organisation Industries"],height=temp["10-100M"],bottom=temp["<1M"]+temp["1-10M"])
        ax.bar(x=temp["Organisation Industries"],height=temp[">100M"],color = "red",bottom=temp["<1M"]+temp["1-10M"]+temp["10-100M"])
        ax.legend(["<1M","1-10M","10-100M",">100M"])
        ax.set_title("Funding by Sector in "+str(year) if year != "All" else "Funding by Sector by all time in €")
        st.pyplot(fig)
