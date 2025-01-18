import streamlit as st

poligono = st.Page("paginas/poligono.py", title="Busca por polígono")
municipio = st.Page("paginas/municipio.py", title="Busca por município")

pg = st.navigation(pages={"Busca": [poligono, municipio]}, expanded=True)

pg.run()