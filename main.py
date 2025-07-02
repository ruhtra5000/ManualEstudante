from experta import *
from engine_parts.facts import *
from engine_parts.engine_instance import ManualEngine
from interface.home import homepageInicial
import streamlit as st

#Arquivo inicial que "limpa" o motor de inferencia
#uma unica vez, cria algumas variáveis na sessão do streamlit, 
#e renderiza a página inicial com streamlit

def inicializarAplicacao():
    if "limpeza" not in st.session_state:
        print("limpo")
        st.session_state['limpeza'] = True
        st.session_state["carregarPagina"] = True
        ManualEngine.reset()

inicializarAplicacao()
homepageInicial()

