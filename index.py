import streamlit as st

poligono = st.Page("paginas/poligono.py", title="Busca por polígono")
municipio = st.Page("paginas/municipio.py", title="Busca por município")
visualizador = st.Page("paginas/visualizador.py", title="Visualizar todos os bens")
contato = st.Page("paginas/contato.py", title="Entre em contato")

pg = st.navigation(pages={"Busca": [municipio, poligono], "Visualizador": [visualizador], "Contato": [contato]}, expanded=True)

pg.run()