import json
import streamlit as st
from utils import pesquisar_municipio
from layout import page_config, hero, disclaimer


# Carregar configuração da página.
page_config()

# Carregar o cabeçalho da página.
hero()


estados = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"]
with open("municipios/est_muni.json", "r", encoding="utf8") as file:
    cidades = json.load(file)

st.write("## Busca por município")

uf = st.selectbox(label="Unidade Federativa", options=estados, placeholder="Selecione a UF", index=None)

with st.form(key="form", border=False):
    if uf:
        municipio = st.selectbox(label="Município", options=cidades[uf], placeholder="Selecione o município", index=None)

        enviado = st.form_submit_button(label="Pesquisar", type="primary")

        if enviado:
            banco_pontos = "sqlite:////home/alexandrecgn/Developer/patrimonio_brasileiro/bens/bens_pt.sqlite"
            tabela_pontos = "pontos"
            resultado = pesquisar_municipio(banco_pontos, tabela_pontos, municipio)
            resultado

# Carregar o disclaimer.
disclaimer()