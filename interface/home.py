import streamlit as st
from engine_parts.engine_instance import ManualEngine
from engine_parts.facts import *

from interface.matricula import matriculaInicial
from interface.disciplina import disciplinaInicial
from interface.cancelamento import cancelamentoInicial
from utils.constants import ABA_LABELS
from interface.avaliacoes import avaliacoesInicial
from interface.faltasAbonos import faltasAbonosInicial
from interface.recursosAdm import recursosAdmInicial
from interface.direitosDeveres import direitosDeveresInicial
from interface.apoioestudantil import apoioEstudantil
from interface.colacaodegrau import colacaoGrau
from interface.estagio import estagio

#Função de carregamento da pagina inicial da aplicação
def homepageInicial():
    st.title("Manual do Estudante")
    abas = st.tabs(ABA_LABELS)

    st.session_state["aba_ativa"] = "Matrícula"

    for i, nome in enumerate(ABA_LABELS):
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
        case "Avaliações e Notas":
            avaliacoesInicial()
        case "Faltas e Abonos":
            faltasAbonosInicial()
        case "Recursos Adm.":
            recursosAdmInicial()
        case "Direitos e Deveres":
            direitosDeveresInicial()
        case "Apoio Estudantil":
            apoioEstudantil()
        case "Colação de Grau":
            colacaoGrau()
        case "Estágio":
            estagio()
            
    #No final, executa o motor — mas apenas se for a aba ativa
    if st.session_state.get("aba_ativa") == opcao:
        ManualEngine.run()
