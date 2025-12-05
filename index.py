import streamlit as st

# Criar um objeto com a página de busca por polígono.
poligono = st.Page("pages/poligono.py", title="Busca por polígono")
# Criar um objeto com a página de contato.
contato = st.Page("pages/contato.py", title="Entre em contato")

# Criar o menu de navegação.
pg = st.navigation(pages={"Busca": [poligono], "Contato": [contato]},
                   expanded=True,
                   position="sidebar",
                   )

# Rodar a navegação com a busca por polígono como página inicial.
pg.run()

# TODO: Adicionar os objetos das páginas do visualizador e da busca por munícipio.