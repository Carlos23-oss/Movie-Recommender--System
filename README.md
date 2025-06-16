# 🎬 Recomendador de Películas

[![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker)](https://www.docker.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-app-red?logo=streamlit)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/Licencia-MIT-green)](LICENSE)

---

Este proyecto es un sistema recomendador de películas, basado en tus gustos cinematográficos y estado de ánimo.

## 🚀 ¿Qué hace?

Recomienda películas similares a una película elegida, usando un modelo de similitud basado en contenido. Tiene una interfaz fácil de usar creada con Streamlit.

## 🧰 Tecnologías utilizadas

- 🐍 Python
- 🎈 Streamlit
- 📦 Pandas, scikit-learn
- 🐳 Docker

## 💻 ¿Cómo ejecutarlo?

### ▶️ Opción 1: Localmente

```bash
git clone https://github.com/Carlos23-oss/recomendador-peliculas.git
cd recomendador-peliculas
pip install -r requirements.txt
streamlit run app/app.py
