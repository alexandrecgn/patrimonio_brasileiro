import streamlit as st

# Criar um objeto com a página inicial
home = st.Page("pages/home.py", title="Página Inicial")
# Criar um objeto com a página de busca por polígono.
poligono = st.Page("pages/poligono.py", title="Busca por polígono")
# Criar um objeto com a página de busca por município.
municipio = st.Page("pages/municipio.py", title="Busca por município")
# Criar um objeto com a página de contato.
contato = st.Page("pages/contato.py", title="Entre em contato")

# Criar o menu de navegação.
pg = st.navigation(pages=[home, poligono, municipio, contato],
                   expanded=True,
                   position="sidebar",
                   )

# Rodar a navegação com a busca por polígono como página inicial.
pg.run()

# TODO: Adicionar o objeto da página do visualizador