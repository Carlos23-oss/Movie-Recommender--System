import streamlit as st
import pandas as pd
from recomendador import cargar_modelo, recomendar_peliculas

st.title("🎬 Recomendador de Películas")

df = pd.read_csv("app/peliculas.csv")
modelo = cargar_modelo()

pelicula = st.selectbox("Selecciona una película:", df["title"].values)

if st.button("Recomendar"):
    recomendaciones = recomendar_peliculas(pelicula, modelo, df)
    st.subheader("Te recomendamos:")
    for rec in recomendaciones:
        st.write("- " + rec)
