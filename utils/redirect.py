"""Arquivo com função de Redirect."""
import streamlit as st


def redirect_page(url):
    """
    Funcão de Redirect.
    
    Args:
        url (str): Url de redirecionamento.
    """
    st.markdown(
        f'<meta http-equiv="refresh" content="0; url={url}">', unsafe_allow_html=True
    )
