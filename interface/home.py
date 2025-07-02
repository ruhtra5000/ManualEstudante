import streamlit as st
from engine_parts.engine_instance import ManualEngine
from engine_parts.facts import *

from interface.matricula import matriculaInicial
from interface.disciplina import disciplinaInicial
from interface.cancelamento import cancelamentoInicial
from interface.apoioestudantil import apoioEstudantil
from interface.colacaodegrau import colacaoGrau
from interface.estagio import estagio

#Função de carregamento da pagina inicial da aplicação
def homepageInicial():
    st.title("Manual do Estudante")
    aba_labels = ["Matrícula", "Disciplina", "Cancel. de Vínculo" , "Apoio Estudantil", "Colação de Grau", "Estágio"]
    abas = st.tabs(aba_labels)

    st.session_state["aba_ativa"] = "Matrícula"

    for i, nome in enumerate(aba_labels):
        with abas[i]:
            processarOpcao(nome)

#Função que carrega cada aba do menu
def processarOpcao(opcao):
    if st.session_state.get("aba_ativa") != opcao:
        st.session_state["aba_ativa"] = opcao
    
    match(opcao):
        case "Matrícula":
            matriculaInicial()
        case "Disciplina":
            disciplinaInicial()
        case "Cancel. de Vínculo":
            cancelamentoInicial()
        case "Apoio Estudantil":
            apoioEstudantil()
        case "Colação de Grau":
            colacaoGrau()
        case "Estágio":
            estagio()
            
    #No final, executa o motor — mas apenas se for a aba ativa
    if st.session_state.get("aba_ativa") == opcao:
        ManualEngine.run()
