import streamlit as st
from engine_parts.engine_instance import ManualEngine
from engine_parts.facts import FaltasAbonosEntrada, ExercicioMilitar
from interface.widgets import campoTexto, campoOpcao

def faltasAbonosInicial():
    st.header("Faltas e Abonos")
    st.write("Aqui você encontra informações sobre faltas, abonos e como solicitar justificativas.")

    # Campo de texto para o usuário digitar a dúvida inicial
    entrada = campoTexto(
        chave="faltas_abonos_geral",
        texto_label="Deseja saber algo mais sobre faltas, abonos ou justificativas?",
        texto_placeholder="Ex.: faltas, abono, justificativa"
    )

    if entrada:
        ManualEngine.declare(FaltasAbonosEntrada(txt=entrada.lower()))
        ManualEngine.imprimirFatos()
    
    # Interfaces
    match st.session_state.get('carregarPagina'):
        # Interfaces principais
        case 'abono':
            abono()

        # Casos de abono
        case 'abonoExercicioMilitar':
            abonoExercicioMilitar()
        case 'abonoInvalido':
            abonoInvalido()
        
def abono():
    opcao = campoOpcao(
        chave='abono',
        texto_label='Você está sob exercício militar?',
        opcoes=['Sim', 'Não']
    )

    if not opcao is None and opcao == 'sim':
        ManualEngine.declare(ExercicioMilitar(tipo=True))

    elif not opcao is None and opcao == 'não':
        ManualEngine.declare(ExercicioMilitar(tipo=False))
        
def abonoExercicioMilitar():
    st.write("Você pode solicitar o abono de faltas devido ao exercício militar. Para isto, apresente a documentação necessária ao setor responsável.")

    st.info(st.session_state.get('explicacao'))

def abonoInvalido():
    st.write("Infelizmente, você não pode solicitar o abono de faltas devido ao exercício militar. Verifique as condições e requisitos.")

    st.info(st.session_state.get('explicacao'))