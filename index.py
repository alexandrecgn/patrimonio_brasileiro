import streamlit as st

poligono = st.Page("pages/poligono.py", title="Busca por polígono")
# municipio = st.Page("pages/municipio.py", title="Busca por município")
# visualizador = st.Page("pages/visualizador.py", title="Bens Culturais")
contato = st.Page("pages/contato.py", title="Entre em contato")

pg = st.navigation(pages={"Busca": [poligono], "Contato": [contato]},
                   expanded=True,
                   position="sidebar",
                   )

pg.run()