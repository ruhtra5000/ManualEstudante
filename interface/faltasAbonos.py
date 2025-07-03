import streamlit as st
from engine_parts.engine_instance import ManualEngine
from engine_parts.facts import FaltasAbonosEntrada, ExercicioMilitar, Gestante, IncapacidadeRelativa
from interface.widgets import campoTexto, campoOpcao

# ======================================================
# Interface inicial para o tratamento de faltas e abonos
# ======================================================
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
        case 'faltas':
            faltas()

        # Tratamentos de abono
        case 'abonoExercicioMilitar':
            abonoExercicioMilitar()
        case 'abonoInvalido':
            abonoInvalido()
        
        # Tratamentos de faltas
        case 'tratamentoGestante':
            tratamentoGestante()
        case 'tratamentoIncapacitadoRelativo':
            tratamentoIncapacitadoRelativo()
        case 'nenhumTratamentoFaltas':
            nenhumTratamentoFaltas()

        # Perguntas
        case 'perguntaIncapacidadeRelativa':
            perguntaIncapacidadeRelativa()

# =====================================
# Interface para o tratamento de abonos
# =====================================
# Pergunta se o usuário está sob exercício militar ou não
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
        
# Interface para o abono de faltas devido ao exercício militar
def abonoExercicioMilitar():
    st.write("Você pode solicitar o abono de faltas devido ao exercício militar. Para isto, apresente a documentação necessária ao setor responsável.")

    st.info(st.session_state.get('explicacao'))

# Interface para o caso de abono inválido
def abonoInvalido():
    st.write("Infelizmente, você não pode solicitar o abono de faltas. Verifique as condições e requisitos.")

    st.info(st.session_state.get('explicacao'))

# =====================================
# Interface para o tratamento de faltas
# =====================================
# Pergunta se o usuário é gestante ou não
def faltas():
    opcao = campoOpcao(
        chave='faltas',
        texto_label='Você é gestante?',
        opcoes=['Sim', 'Não']
    )

    if not opcao is None and opcao == 'sim':
        ManualEngine.declare(Gestante(tipo=True))

    elif not opcao is None and opcao == 'não':
        ManualEngine.declare(Gestante(tipo=False))

# Pergunta se o usuário tem alguma incapacidade relativa ou temporária
def perguntaIncapacidadeRelativa():
    resposta = campoOpcao(
        chave='incapacidade_relativa',
        texto_label='Você tem alguma incapacidade relativa ou temporária?',
        opcoes=['Sim', 'Não']
    )

    if not resposta is None and resposta == 'sim':
        ManualEngine.declare(IncapacidadeRelativa(tipo=True))
    elif not resposta is None and resposta == 'não':
        ManualEngine.declare(IncapacidadeRelativa(tipo=False))

# Interface caso o usuário tenha alguma incapacidade relativa ou temporária
def tratamentoIncapacitadoRelativo():
    st.write("Você pode solicitar o abono de faltas devido a uma incapacidade relativa ou temporária. Para isto, apresente a documentação necessária ao setor responsável.")

    st.info(st.session_state.get('explicacao'))

# Interface caso o usuário seja gestante
def tratamentoGestante():
    st.write("Você pode solicitar o abono de faltas devido à gestação. Para isto, apresente a documentação necessária ao setor responsável.")

    st.info(st.session_state.get('explicacao'))

# Interface caso o usuário não possa solicitar o abono de faltas
def nenhumTratamentoFaltas():
    st.write("Infelizmente, você não pode solicitar o abono de faltas. Verifique as condições e requisitos.")

    st.info(st.session_state.get('explicacao'))