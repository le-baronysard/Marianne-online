import streamlit as st

st.balloons()

col1, col2 = st.columns(2)

with col1 : 
    st.image("data/marianne.jpeg", width=200)
with col2 :
    st.header("Marianne Lahana")
    
    st.markdown(""" 
                Avocate en droit de la santé    
                Docteure en droit public   
                Doctorante en sciences politiques  
                [![LinkedIn](https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg)](https://www.linkedin.com/in/marianne-lahana-95593167/)
                            """)
    
container = st.container(border=True)

container.markdown("""Dans le cadre de sa thèse de sciences politiques réalisée au sein
de l’Université Sorbonne Paris-Nord sous la direction de
Monsieur Jean-René Garcia, Marianne Lahana a souhaité
rassembler les données des entreprises de santé innovantes en
France concernant notamment leur levée de fonds. Sa thèse
intitulée « De l’évolution des politiques publiques sur
l’innovation en santé » est une étude pluridisciplinaire qui
permet, grâce à l’extraction et l’analyse des données 
récupérées en accès libre sur internet, de mieux comprendre le rôle des pouvoirs publics dans l’accompagnement des
nouvelles entreprises innovantes. Ce site dédié rassemble ainsi les données de plus de 500
entreprises de santé et offre une lecture globale des levées de fond opérées de la création
des entreprises jusqu’en décembre 2023.""")


col21, col22 = st.columns(2)
with col1 : 
    st.image("https://media.licdn.com/dms/image/C4D03AQEGERkv_Bawgg/profile-displayphoto-shrink_400_400/0/1647530834999?e=1720051200&v=beta&t=d_SuFCfUIdX2-Id3YGLtOXqjDZZU3xw-yj9v6QT2l_I", width=200)
with col2 :
    st.header("Aloys Bernard")
    
    st.markdown(""" 
                Data Scientist  
                [![LinkedIn](https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg)](https://www.linkedin.com/in/aloys-bernard/)
                            """)
