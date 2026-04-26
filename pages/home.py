import streamlit as st
from layout import hero, page_config, disclaimer

# Carregar configuração da página.
page_config()

# Carregar o cabeçalho da página.
hero()

with st.container(border=False):
        st.write("### O que é isso?")
        st.write("""
                 Esse é um espaço de experimentação com os dados disponibilizados\
                 publicamente sobre o Patrimônio Cultural protegido em nível federal.
                 
                 Através da [Busca por polígono](https://patrimoniobrasileiro.com.br/poligono)\
                 é possível inserir uma poligonal e o resultado será exibido em um mapa com\
                 todos os bens georreferenciados encontrados dentro dessa poligonal.

                 Na [Busca por município](https://patrimoniobrasileiro.com.br/municipio)\
                 é possível selecionar UF e município para ver uma tabela com\
                 todos os bens georreferenciados encontrados na cidade selecionada.

                 Futuramente serão adicionadas as funcionalidades de mapa em **Busca por Município** e\
                 uma página para **visualização de todos os bens georreferenciados**.
        """)
        st.write("")
        st.write("*Este projeto está em desenvolvimento: versão alpha* [`v0.18`](https://github.com/alexandrecgn/patrimonio_brasileiro/releases/tag/v0.18)")

with st.container(
    border=True,
):
    st.write("### Bens culturais com geolocalização")
    
    with st.container(
    border=False,
    horizontal=True,
    horizontal_alignment="distribute"
):
        st.metric(label="**Bens Arqueológicos**", value=31.671, delta="Primeira medição", border=True, width="content", delta_color="off", delta_arrow="off")
        st.metric(label="**Bens Imateriais\***", value=330, delta="Primeira medição", border=True, width="content", delta_color="off", delta_arrow="off")
        st.metric(label="**Bens Tombados**", value=1158, delta="Primeira medição", border=True, width="content", delta_color="off", delta_arrow="off")
        st.metric(label="**Bens Ferroviários**", value=596, delta="Primeira medição", border=True, width="content", delta_color="off", delta_arrow="off")
        st.metric(label="**Data de atualização**", value="19 de abril de 2026", delta="Primeira medição", border=True, width="content", delta_color="off", delta_arrow="off")

    st.warning("\* *Esse número corresponde ao total de pontos de ocorrência de Bens Imateriais. O total de Bens Imateriais Registrados nos Livros de Registro é 65.*")

with st.container(border=True):
    st.write("### Fonte dos dados")
    st.write("""
- Bens Arqueológicos: https://www.gov.br/iphan/pt-br/patrimonio-cultural/patrimonio-arqueologico
- Bens Imateriais: https://bcr.iphan.gov.br/
- Bens Tombados: http://portal.iphan.gov.br/pagina/detalhes/126
- Bens Ferroviários: http://portal.iphan.gov.br/pagina/detalhes/127
- Dados de geolocalização: https://geoserver.iphan.gov.br/
""")


# Carregar o disclaimer.
disclaimer()