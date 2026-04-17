import streamlit as st


def page_config():
     # Definir o layout da página como "wide".
     st.set_page_config(layout="wide")
     #Definir logo do site
     st.logo(image="logos/logo.svg", size="large")


def hero():
    # Criar o cabeçalho das páginas.
    with st.container(key="hero",
                      border=False,
                      horizontal=False,
                      horizontal_alignment="center",
                      vertical_alignment="top",
                      ):
            st.image(image="logos/logo.svg")
            # st.markdown("# **patrimônio_brasileiro.**", width="content")

            # with st.container(
            #      horizontal=True,
            #      horizontal_alignment="center",
            #      ):
            #     st.markdown("*patrimônio*", width="content")
            #     st.markdown("*&*", width="content")
            #     st.markdown("*dados*", width="content")
            #     st.markdown("*&*", width="content")
            #     st.markdown("*experimentação*", width="content")


def disclaimer():
    # Criar o disclaimer do fim de cada página.
    st.write("----")
    st.error("**Disclaimer:** Este projeto não possui nenhum vínculo com o Instituto do Patrimôno Histórico e Artístico Nacional - IPHAN ou qualquer outro órgão/instuição.")


if __name__ == "__main__":
    print("Esse arquivo não deve ser executado!")