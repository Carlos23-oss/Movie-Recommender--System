# Sistema Recomendador de Películas 🎥

Este proyecto muestra un recomendador de películas basado en similitudes.

## Cómo ejecutar

```bash
docker build -t recomendador-peliculas .
docker run -p 8501:8501 recomendador-peliculas
```

Accede en el navegador a: `http://localhost:8501`
# 🎬 Movie Recommender System

An intelligent movie recommender based on your **cinematic preferences** and **mood**. Built with **Python**, powered by **Streamlit**, and ready for production with **Docker**.

[![Streamlit App](https://img.shields.io/badge/Streamlit-Online%20Demo-red?logo=streamlit)](https://streamlit.io/)
[![Dockerized](https://img.shields.io/badge/docker-ready-blue?logo=docker)](https://hub.docker.com/)
[![Python](https://img.shields.io/badge/python-3.10+-yellow.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

---

## 🚀 What does this project do?

🔎 This movie recommender:
- Suggests similar movies based on your input.
- Uses a basic content similarity model (can be extended with embeddings or FAISS).
- Provides a clean interface via Streamlit for fast and easy interaction.

---

## 🧩 Project Structure

