import streamlit as st
from engine_parts.engine_instance import ManualEngine
from engine_parts.facts import *
from interface.widgets import campoTexto

def cancelamentoInicial():
    st.header("Cancelamento de vínculo")
    st.markdown('''O cancelamento de registro acadêmico/vínculo representa o :blue-background[desligamento efetivo] da UFAPE.''')