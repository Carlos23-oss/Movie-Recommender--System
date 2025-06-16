import pandas as pd
import pickle

def cargar_modelo():
    with open("app/model.pkl", "rb") as f:
        modelo = pickle.load(f)
    return modelo

def recomendar_peliculas(titulo, modelo, df_peliculas):
    if titulo not in df_peliculas["title"].values:
        return ["Película no encontrada."]
    idx = df_peliculas[df_peliculas["title"] == titulo].index[0]
    sim_scores = list(enumerate(modelo[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    recomendaciones = [df_peliculas.iloc[i[0]]["title"] for i in sim_scores[1:6]]
    return recomendaciones
