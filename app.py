"""Arquivo referente ao Do Zero To Know What."""
import streamlit as st
import base64

from paginas.linuxdocker import linuxdocker

icon = "assets/projeto.png"
st.set_page_config(page_title="Do Zero To Know What", page_icon=icon, layout="wide")


def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bin_str}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('assets/background.png')

st.image("assets/projeto.png", width=150)
st.title("Do Zero To Know What")
st.subheader(":book: Seja bem-vindo(a) ao programa de Do Zero To Know What!")
st.write(
    "A ideia deste projeto é que você possa aprender de maneira muito simples,n\
          tirando vezes de um zero para um conhecimento solido, onde poderar seguir um bom caminho de aprendizado prático e profissonal."
)


st.subheader("Quem são os Instrutores?")
col1, col2 = st.columns(2)
with col1:
    st.image("assets/wallace.jpg", width=300)
    st.markdown(
        "- [Wallace Camargo - Data Engineer](https://www.linkedin.com/in/wallace-camargo-35b615171/)"
    )
with col2:
    st.image("assets/luhborba.jpg", width=300)
    st.markdown(
        "- [Luciano Borba - Data Manager](https://www.linkedin.com/in/luhborba/)"
    )


with st.expander("Workshops Disponíveis:"):
    menu1 = st.tabs(["Desbravando Linux e Docker"])
    with menu1[0]:
        linuxdocker()


st.markdown(
    """
            ## Benefícios do Projeto

            - Acesso Vitalicio ao Conteudo
            - Aulas Ao Vivo e Hands-on (No Lançamento)
            - Acesso as Gravações
            - Certificado de Conclusão
            - Suporte Simplificado
            - Comunidade Exclusiva

            """
)
