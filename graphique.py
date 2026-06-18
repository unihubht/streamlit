import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 Analyse interactive des variables")

uploaded_file = st.file_uploader("Importer un fichier CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset")
    st.write(df.head())

    # Choix de la variable
    variable = st.selectbox("Choisir une variable à analyser :", df.columns)

    # Choix du type de graphique
    chart_type = st.radio(
        "Choisir le type de graphique :",
        ["Histogramme", "Boxplot", "Bar chart", "Heatmap"]
    )

    # Numérique
    if pd.api.types.is_numeric_dtype(df[variable]):
        if chart_type == "Histogramme":
            st.subheader(f"Histogramme de {variable}")
            fig, ax = plt.subplots()
            sns.histplot(df[variable].dropna(), kde=True, ax=ax, color="skyblue")
            st.pyplot(fig)

        elif chart_type == "Boxplot":
            st.subheader(f"Boxplot de {variable}")
            fig, ax = plt.subplots()
            sns.boxplot(x=df[variable].dropna(), ax=ax, color="lightgreen")
            st.pyplot(fig)

        elif chart_type == "Heatmap":
            st.subheader("Heatmap des corrélations")
            fig, ax = plt.subplots(figsize=(8,6))
            sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

    # Catégorielle
    else:
        if chart_type == "Bar chart":
            st.subheader(f"Diagramme en barres de {variable}")
            fig, ax = plt.subplots()
            df[variable].value_counts().plot(kind="bar", ax=ax, color="orange")
            st.pyplot(fig)
        else:
            st.warning("⚠️ Ce type de graphique n'est pas adapté aux variables catégorielles.")
