import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

st.title("⚙️ Entraîner votre modele ici ")

uploaded_file = st.file_uploader("Importer un fichier CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset brut")
    st.write(df.head())

    # Nettoyage basique
    df = df.drop_duplicates()
    df = df.dropna()

    # Encodage des variables catégorielles
    for col in df.select_dtypes(include="object").columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

    st.subheader("Dataset nettoyé")
    st.write(df.head())

    # Choix de la cible et des features
    target = st.selectbox("Choisir la variable cible (Y) :", df.columns)
    features = st.multiselect("Choisir les variables explicatives (X) :", [col for col in df.columns if col != target])

    if target and features:
        X = df[features]
        y = df[target]

        # Normalisation
        scaler = StandardScaler()
        X = scaler.fit_transform(X)

        # Division train/test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # Entraînement
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Résultats complets
        st.subheader("Résultats de l'entraînement")
        st.write("✅ Accuracy :", accuracy_score(y_test, y_pred))
        st.write("🎯 Precision :", precision_score(y_test, y_pred, average="weighted"))
        st.write("📌 Recall :", recall_score(y_test, y_pred, average="weighted"))
        st.write("⚖️ F1-score :", f1_score(y_test, y_pred, average="weighted"))
        st.text("Rapport de classification détaillé :")
        st.text(classification_report(y_test, y_pred))
        st.success("🎉 Entraînement terminé avec succès !")
        st.balloons()