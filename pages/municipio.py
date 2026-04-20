import json
import streamlit as st
from layout import page_config, hero, disclaimer


# Carregar configuração da página.
page_config()

# Carregar o cabeçalho da página.
hero()


estados = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"]
with open("municipios/est_muni.json", "r", encoding="utf8") as file:
    cidades = json.load(file)

uf = st.selectbox(label="Unidade Federativa", options=estados, placeholder="Selecione a UF", index=None)

if uf:
    municipio = st.selectbox(label="Município", options=cidades[uf], placeholder="Selecione o município", index=None)


# Carregar o disclaimer.
disclaimer()