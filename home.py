import streamlit as st
# Titre principal
st.title("✨ Bienvenue sur notre note d'accueil ✨")
# Sous-titre
st.header("Nous sommes très contents de vous accueillir")

# Texte introductif
st.write("""
Bienvenue dans cette application de démonstration. 
Ici, vous pouvez explorer différentes étapes du **machine learning** :
- [Importation des données](ca://s?q=Importation_données)
- [Analyse exploratoire](ca://s?q=Analyse_exploratoire)
- [Subdivision du dataset](ca://s?q=Subdivision_dataset)
- [Entraînement du modèle](ca://s?q=Entraînement_modèle)
- [Prédiction](ca://s?q=Prédiction_modèle)
- [Évaluation](ca://s?q=Évaluation_modèle)

C’est un premier pas vers des projets plus ambitieux, notamment dans la **[santé](ca://s?q=Projets_machine_learning_santé)** et d’autres domaines utiles.
""")

# Message de remerciement
st.success("🙏 Merci à Aboubacar pour son orientation et à TechnoDev pour cette formation qui nous ouvre la voie vers le déploiement et le deep learning.")
