import streamlit as st
from layout import hero, page_config, disclaimer

# Carregar configuração da página.
page_config()

# Carregar o cabeçalho da página.
hero()


# Exibir informações de contato.
st.write("### Entre em contato")

st.write(
    """
Para sugerir melhorias ou reportar erros: suporte@patrimoniobrasileiro.com.br
\n
Para contato geral: contato@patrimoniobrasileiro.com.br
"""
)

# Carregar o disclaimer.
disclaimer()