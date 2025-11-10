import streamlit as st


def hero():
    with st.container(horizontal_alignment="center"):
        st.title("Patrimônio Brasileiro", width="content")
        st.write("---")


if __name__ == "__main__":
    print("Esse arquivo não deve ser executado!")