"""Arquivo referente ao Workshop Linux Docker."""
import streamlit as st

from utils.redirect import redirect_page


def linuxdocker():
    """Funcão referente ao Workshop Linux Docker."""
    st.markdown(
        """
                    ### O que aprenderei neste projeto?

                    - Qual problema a ferramenta resolve
                    - Quando foi inventada
                    - Quais empresas usam
                    - Vagas no Linkedin
                    - Como Instalar a ferramenta
                    - Quem são as referências da área
                    - Como utilizar em Mundo Real
                    - Um projeto bem próximo do mundo real

                    ### Perguntas Frequentes:

                    *Quando serão as aulas?*
                    - 18/06/2024 - 20h às 22h
                    - 20/06/2024 - 20h às 22h

                    *As aulas ficarão gravadas?*
                    - Sim

                    *Durante quanto tempo posso acessar o conteúdo gravado?*
                    - Vitalício

                    *Terá material de apoio?*
                    - Sim

                    *Como tirar as dúvidas?* 
                    - Na nossa comunidade do Slack

                    *Terá certificado de conclusão?*
                    - Sim

                    *Qual o valor do investimento?*
                    - 1º lote - R$ 97,00 até 12/06
                    - 2º lote - R$ 147,00 após 13/06
                    """
    )
    if st.button("Comprar"):
        redirect_page("https://pay.kiwify.com.br/lzHO5th")
