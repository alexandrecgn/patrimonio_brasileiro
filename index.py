import streamlit as st

poligono = st.Page("paginas/poligono.py", title="Busca por polígono")
municipio = st.Page("paginas/municipio.py", title="Busca por município")
visualizador = st.Page("paginas/visualizador.py", title="Visualizar todos os bens")

pg = st.navigation(pages={"Busca": [poligono, municipio], "Visualizador": [visualizador]}, expanded=True)

pg.run()