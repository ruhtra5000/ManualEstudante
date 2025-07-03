import streamlit as st
from engine_parts.engine_instance import ManualEngine
from engine_parts.facts import RecursosAdmEntrada
from interface.widgets import campoTexto, campoOpcao

# Página inicial de recursos administrativos
def recursosAdmInicial():
    st.header("Recursos Administrativos")
    st.write("Aqui você encontra informações sobre recursos administrativos, como abonos, faltas, e revisão de provas.")

    # Campo de texto para o usuário digitar a dúvida inicial
    entrada = campoTexto(
        chave="recursosAdm_geral",
        texto_label="Deseja saber algo mais sobre recursos administrativos?",
        texto_placeholder="Ex.: reapreciação, recurso"
    )

    if entrada:
        ManualEngine.declare(RecursosAdmEntrada(txt=entrada.lower()))
        ManualEngine.imprimirFatos()

    match st.session_state.get('carregarPagina'):
        case 'reapreciação':
            reapreciacao()
        case 'recurso':
            recurso()

# Interface para reapreciação de decisão
def reapreciacao():
    st.header("Reapreciação de Decisão")
    
    st.write("O caso de reapreciação de decisão é uma das duas instâncias recursais disponíveis para o(a) aluno(a) da UFAPE que se sentir prejudicado(a) por qualquer decisão tomada pela Universidade.")
    
    st.write("Para este e outros processos administrativos (com exceção da revisão de nota, que tem um prazo diferente), o prazo regimental é de 05 dias úteis, contados a partir da ciência da decisão administrativa e o pedido deve ser dirigido à autoridade que a proferiu.")
    
    st.warning("Caso haja recusa ou a decisão administrativa seja mantida após a reapreciação, o(a) aluno(a) pode então recorrer à instância superior à autoridade, que geralmente é um conselho superior")

# Interface para recurso administrativo
def recurso():
    st.header("Recurso à instância superior")
    
    st.write("É a segunda das duas instâncias recursais disponíveis para o(a) estudante da UFAPE que se sentir prejudicado(a) por uma decisão da Universidade.")
    
    st.write("Este recurso cabe caso haja recusa do pedido de reapreciação da decisão inicial ou se a decisão administrativa for mantida após a reapreciação. Ou seja, é uma etapa subsequente à 'reapreciação de decisão', que é julgada pela mesma autoridade que emitiu a decisão original.")

    st.warning("Para este processo, assim como para os demais processos administrativos (com exceção da revisão de nota, que tem um prazo específico de 48 horas), o prazo regimental é de 05 dias úteis. Esse prazo é contado a partir da ciência da decisão administrativa e o recurso deve ser dirigido à autoridade que a proferiu")