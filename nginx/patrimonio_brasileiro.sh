#!/bin/bash


# Acidionar caminnho para o Streamlit
export PATH=/home/alexandrecgn/DevOps/buscador_do_patrimônio/.venv/bin:$PATH

# Mudar para diretório do Patrimônio Brasileiro
cd /home/alexandrecgn/DevOps/buscador_do_patrimônio

# Ativar Venv
source .venv/bin/activate

# Iniciar servidor do Streamlit
streamlit run index.py
