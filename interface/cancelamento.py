import streamlit as st
from engine_parts.engine_instance import ManualEngine
from engine_parts.facts import *
from interface.widgets import campoTexto, campoOpcao, campoNumero

#Arquivo direcionado a interface da aba de cancelamento de vínculo

#Parte inicial da interface
def cancelamentoInicial():
    st.header("Cancelamento de vínculo")
    st.markdown('''O cancelamento de registro acadêmico/vínculo representa o :blue-background[desligamento efetivo] da UFAPE.''')

    entrada = campoTexto (
        'cancelamentoVinculo', 
        'Deseja saber algo mais sobre cancelamento de vínculo?',
        'Ex.: Abandono, Desligamento, Penalidade, Transferencia, Reintegraçao'
    )

    if entrada:
        ManualEngine.declare(CancelamentoEntrada(txt=entrada))
        ManualEngine.imprimirFatos()
        ManualEngine.run()

    match(st.session_state.get('carregarPagina')):
        case 'abandonoCurso':
            abandonoCurso()
        case 'desligamentoVinculo':
            desligamentoVinculo()
        case 'desligamentoVinculoNegativo':
            desligamentoVinculoNegativo()
        case 'penalidadeDisciplinar':
            penalidadeDisciplinar()
        case 'transferencia':
            transferencia()
        case 'reintegracao':
            reintegracao()
        case 'reintegracaoNegativa':
            reintegracaoNegativa()
        
        #Perguntas
        case 'perguntaTempoRestante':
            perguntaTempoRestante()
        case 'perguntaTrancamentos':
            perguntaTrancamentos()
        case 'perguntaReprovacao':
            perguntaReprovacao()
        case 'perguntaAnosEvasao':
            perguntaAnosEvasao()

#Interface sobre abandono do curso
def abandonoCurso():
    st.write("Se o(a) aluno(a) não se matricular no período " + 
            "fixado no Calendário Acadêmico, perderá vínculo/vaga com a " +
            "Instituição, configurando-se como abandono de curso.")
    
    st.info(st.session_state.get('explicacao'))

#Interface sobre desligamento de vínculo positivo
def desligamentoVinculo():
    st.write("Provavelmente, você será desvinculado da universidade. Recomendo " +
             "entrar em contato com a coordenação do seu curso. De toda forma: " + 
             "O aluno(a) poderá regressar à UFAPE, se desejar, prestando novo processo " +
             "seletivo e pedindo aproveitamento de disciplina.")

    st.info(st.session_state.get('explicacao'))

#Interface sobre desligamento de vínculo negativo
def desligamentoVinculoNegativo():
    st.write("Você está bem, sem chances de ter seu vínculo cancelado.")

    st.info(st.session_state.get('explicacao'))

#Interface para penalidade disciplinar
def penalidadeDisciplinar():
    st.write("A exclusão do(a) aluno(a) da Universidade " +
            "poderá ocorrer da aplicação de penalidade disciplinar, depois de " +
            "apuradas as causas em forma processual.")

    st.info(st.session_state.get('explicacao'))

#Interface para transferencia entre universidades
def transferencia():
    st.write("O(a) aluno(a) poderá requerer transferência de seu " +
            "curso para outra Instituição de Ensino Superior, voluntariamente ou ex-" +
            "officio (para acompanhar seus genitores ou tutores, que sejam " +
            "funcionários públicos ou militares); para tanto, deverá manter o vínculo " +
            "na Universidade (estar regularmente matriculado), até que a outra " +
            "Instituição envie a declaração de vaga e o aceite.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para casos de reintegração possíveis
def reintegracao():
    st.write("Você pode requerer a reintegração, uma " +
            "única vez, no mesmo curso (inclusive para colação de grau). " +
            "Entre em contanto com a coordenação do seu antigo curso para " + 
            "mais informações.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para casos de reintegração não possíveis
def reintegracaoNegativa():
    st.write("Você não pode requerer a reintegração. Portanto, " + 
             "é preciso realizar um novo processo seletivo para que " +
             "haja um novo ingresso.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para pergunta sobre se o curso é "finalizavel" no tempo restante
def perguntaTempoRestante():
    resposta = campoOpcao (
        'tempoRestanteCurso',
        'Com todas as disciplinas que restam, você ainda é capaz de integralizar o currículo do seu curso?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(TempoRestanteCurso(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(TempoRestanteCurso(tipo = True))

#Interface para pergunta sobre trancamentos realizados
def perguntaTrancamentos():    
    resposta = campoNumero (
        'trancamentosCancelamento',
        'Quantos períodos você já trancou? Sejam eles consecutivos ou alternados.',
        0,
        4
    )
    
    if not resposta is None:
        ManualEngine.declare(Trancamentos(valor = resposta))

#Interface para pergunta sobre reprovações numa mesma matéria
def perguntaReprovacao():
    resposta = campoOpcao (
        'reprovacaoMateria',
        'Você já foi reprovado 4 vezes numa mesma matéria (por nota ou falta)?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(ReprovacoesMesmaMateria(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(ReprovacoesMesmaMateria(tipo = True))

#Interface para pergunta sobre quantidade de anos de evasão
def perguntaAnosEvasao():
    resposta = campoNumero(
        'anosEvasao',
        'Caso você tenha perdido o vínculo com a UFAPE, há quantos anos você está desvinculado?',
        0,
        20
    )

    if not resposta is None:
        ManualEngine.declare(AnosEvasao(valor = resposta))