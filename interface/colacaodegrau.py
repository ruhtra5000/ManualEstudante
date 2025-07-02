import streamlit as st
from engine_parts.engine_instance import ManualEngine
from engine_parts.facts import *
from interface.widgets import campoTexto

def colacaoGrau():
    st.header("Colação de Grau")
    st.write(
        "A colação de grau ocorre após o(a) aluno(a) integralizar todos os componentes do curso, incluindo o ENADE e as atividades complementares. " +
        "Ela é realizada em sessão solene e pública com todos os cursos de graduação, presidida pelo(a) Reitor(a) da UFAPE.")

    entrada = campoTexto(
        chave="colacao_grau",
        texto_label="Deseja saber algo mais sobre colação de grau?",
        texto_placeholder="Ex.: colação em separado, aluno laureado"
    )

    if entrada:
        ManualEngine.declare(ColacaoGrauEntrada(txt=entrada))
        ManualEngine.imprimirFatos()
