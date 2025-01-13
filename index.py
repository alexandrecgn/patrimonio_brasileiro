import streamlit as st

poligono = st.Page("pages/poligono.py", title="Busca por polígono")
municipio = st.Page("pages/municipio.py", title="Busca por município")

pg = st.navigation(pages=[poligono, municipio], expanded=True)

pg.run()