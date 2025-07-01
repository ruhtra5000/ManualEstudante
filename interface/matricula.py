import streamlit as st
from engine_parts.engine_instance import ManualEngine
from engine_parts.facts import *
from interface.widgets import campoTexto

def matriculaInicial():
    st.header("Matrícula")
    st.write("Também conhecida como Registro Acadêmico, é a vinculação do(a) "+
                "estudante a um curso da Instituição nas datas previstas no Calendário "+
                "Acadêmico disponível no site da UFAPE.")
            
    entrada = campoTexto(
        chave="matricula",
        texto_label="Deseja saber algo mais sobre matrícula?",
        texto_placeholder="Ex.: semestre, reajuste"
    )
    if entrada:
        ManualEngine.declare(MatriculaEntrada(txt=entrada))
        ManualEngine.imprimirFatos()