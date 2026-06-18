import streamlit as st 

pages={
    "menu":[
        st.Page("home.py", title="accueil"),
        st.Page("apropos.py ", title=" a Propos"),
        st.Page("data.py", title=" visualisation donnees"),
         st.Page("graphique.py", title="affichage-graphique")


    ],
    "administration":[
        st.Page("administration.py", title="administration"),
    ],
      "Modele-entrainement":[
        st.Page("modele.py", title="modele-entrainement"),
    ],
}
nav=st.navigation(pages, position="sidebar")
nav.run()




