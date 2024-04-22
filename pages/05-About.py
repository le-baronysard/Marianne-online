import streamlit as st

class TeamMember:
    def __init__(self, name,role, linkedin):
        self.name = name
        self.role = role
        self.linkedin = linkedin

    def introduce(self):
        st.write(f"{self.role} ")
        st.write(f"Connect on LinkedIN: [{self.name}]({self.linkedin}).")

marianne = TeamMember("Marianne", """Mon secteur d'activité est la responsabilité médicale et l'accompagnement des entreprises de santé dans leurs problématiques juridiques et règlementaires. \n J'accompagne les professionnels de santé et les industriels dans leur problématique de responsabilité, médicale/dommage corporel, de relation avec les instances ordinales, d'utilisation de leurs dispositifs innovants/intelligence artificielle, propriété intellectuelle, contrats de partenariats..."""
, "https://www.linkedin.com/in/marianne-lahana-95593167/")
#aloys = TeamMember("Aloys", "data analyst", "https://www.linkedin.com/in/aloys")


st.header("Marianne la banane")
st.image("data/marianne.jpeg", width=200)
marianne.introduce()
