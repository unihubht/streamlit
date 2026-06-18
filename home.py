import streamlit as st

# Titre principal
st.title("✨ Bienvenue sur notre application ✨")

# Sous-titre
st.header("Nous sommes très heureux de vous accueillir")

# Texte d'accueil en plusieurs paragraphes
st.write("""
Cette application est conçue pour vous offrir une première expérience pratique 
dans le domaine du machine learning. Elle vous permet de découvrir et de tester 
les principales étapes d’un projet de données.

Vous pourrez explorer le processus complet : importation des données, 
analyse exploratoire, subdivision du dataset, entraînement du modèle, 
prédiction et évaluation.

C’est une étape importante qui montre comment transformer des données 
brutes en résultats utiles. Elle constitue une base solide pour avancer 
vers des projets plus ambitieux.

Nous remercions chaleureusement Aboubacar pour son orientation, ainsi que 
TechnoDev pour cette formation. Grâce à ces bases, nous allons continuer 
à progresser et travailler sur des projets plus directs, notamment dans 
le domaine de la santé et d’autres secteurs utiles.
""")

# Message final
st.success("🚀 Merci de votre visite, et bonne exploration !")
