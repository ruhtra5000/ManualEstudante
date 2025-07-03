# interface/avaliacoes.py
import streamlit as st
from engine_parts.engine_instance import ManualEngine
from engine_parts.facts import AvaliacaoEntrada, PrazoRevisaoOK
from interface.widgets import campoTexto, campoOpcao

# Função inicial da aba "Avaliações e Notas"
def avaliacoesInicial():
    st.header("Avaliações e Notas")
    st.write("Aqui você encontra informações sobre seu rendimento acadêmico, avaliações, e o processo de revisão de notas.")

    # Campo de texto para o usuário digitar a dúvida inicial
    entrada = campoTexto(
        chave="avaliacoes_geral",
        texto_label="Deseja saber algo mais sobre avaliações, notas ou revisão de provas?",
        texto_placeholder="Ex.: revisão, frequência, média"
    )

    if entrada:
        ManualEngine.declare(AvaliacaoEntrada(txt=entrada.lower()))
        ManualEngine.imprimirFatos()

    match st.session_state.get('carregarPagina'):
        # Interfaces principais
        case 'revisaoProva':
            revisaoProva()

        # Casos de revisão
        case 'revisaoPrazoOK':
            revisaoPrazoOK()
        case 'revisaoPrazoExpirado':
            revisaoPrazoExpirado()

def revisaoProva():
    
    resposta = campoOpcao(
        chave='revisaoProva',
        texto_label='Você está requerindo a revisão da prova dentro dum prazo de 48h após a publicação da mesma?',
        opcoes=['Sim', 'Não']
    )

    if not resposta is None and resposta == 'sim':
        ManualEngine.declare(PrazoRevisaoOK(tipo=True))
    
    elif not resposta is None and resposta == 'não':
        ManualEngine.declare(PrazoRevisaoOK(tipo=False))

def revisaoPrazoOK():
    st.write("Você pode solicitar a revisão da prova! Para isto, entre em contato com o professor responsável pela disciplina.")

    st.info(st.session_state.get('explicacao'))

def revisaoPrazoExpirado():
    st.write("Infelizmente, o prazo para solicitar a revisão da prova já expirou. Você não poderá mais solicitar a revisão.")

    st.info(st.session_state.get('explicacao'))