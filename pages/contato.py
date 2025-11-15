import streamlit as st
from layout import hero, page_config, disclaimer


page_config()


hero()


st.write("### Entre em contato")

st.write(
    """
Para sugerir melhorias ou reportar erros: suporte@patrimoniobrasileiro.com.br
\n
Para contato geral: contato@patrimoniobrasileiro.com.br
"""
)


disclaimer()