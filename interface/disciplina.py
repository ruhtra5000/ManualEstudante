import streamlit as st
from engine_parts.engine_instance import ManualEngine
from engine_parts.facts import *
from interface.widgets import campoTexto

def disciplinaInicial():
    st.header("Disciplina")
    st.write("Uma disciplina é um componente curricular que abrange um conjunto específico " +
             "de conhecimentos e atividades, geralmente relacionados a uma área de estudo. " + 
             "É uma unidade de ensino dentro de um curso, com conteúdo programático definido, " + 
             "carga horária e, muitas vezes, pré-requisitos.")
    
    entrada = campoTexto(
        chave="disciplina",
        texto_label="Deseja saber algo mais sobre disciplinas?",
        texto_placeholder="Ex.: cancelamento, dispensa"
    )
    if entrada:
        ManualEngine.declare(DisciplinaEntrada(txt=entrada))
        ManualEngine.imprimirFatos()