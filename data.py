import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt   # ✅ Import obligatoire

st.title("bienvenue sur notre page d'analyse de  ")
st.header("importer votre jeu de donnees")

upload_file=st.file_uploader("import un ficheier csv, ou xlxl", type=["csv", "xlsx"])

if upload_file is not None:
    # Lire le fichier avec pandas
    df=pd.read_csv(upload_file)
    st.success("votre jeu de donnees est impporte bravo")

    # afficher un appercue
    st.header(" les 6 premieres lignes du dataset" )
    st.subheader("Aperçu du jeu de données")
    st.write(df.head())

      # Dimensions
    st.header(" Dimensions du votre dataset" )

    st.write(f"Nombre de lignes : {df.shape[0]}")
    st.write(f"Nombre de colonnes : {df.shape[1]}")

    # affichage des differences champs du dataset
    st.header("affichage des differences champs du dataset" )
    names= st.write(list(df.columns))
    st.write(names)

    #resume de tous les variable 
    st.header("resume de toutes les variables" )
    resume=resume=df.describe(include='all')
    st.write(resume)

    # netoyage du dataset: 
    st.subheader("netoyage du dataset")
    # Supprimer les espaces dans les noms de colonnes
    df.columns=df.columns.str.strip()

    # Supprimer les espaces dans les valeurs textuelles
    df=df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Remplacer les valeurs manquantes par NaN
    df=df.replace(["", " ", "None", "nan"], pd.NA)

    st.write("affichage du dataset netoyer")
    # Afficher le dataset nettoyé
    st.write("✅ Dataset nettoyé")
    st.write(df.head())

    #tracer un graqphique plt pour ce jeu donnees , regression lineaire
    st.subheader("Histogramme")
    col_num = st.selectbox("Choisir une variable numérique :", df.select_dtypes(include="number").columns)
    fig, ax = plt.subplots()
    sns.histplot(df[col_num].dropna(), kde=True, ax=ax)
    st.pyplot(fig)
else: 
    st.markdown("""
                impossible de charger ce jeu de donnnes ou format incorrect, \n
                uniquement format CSV
                """)