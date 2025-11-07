#!/bin/bash


# Acidionar caminnho para o Streamlit
export PATH=/home/alexandrecgn/patrimonio_brasileiro/.venv/bin:$PATH

# Mudar para diretório do Patrimônio Brasileiro
cd /home/alexandrecgn/patrimonio_brasileiro

# Ativar Venv
source .venv/bin/activate

# Iniciar servidor do Streamlit
streamlit run index.py