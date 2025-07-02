import streamlit as st
from engine_parts.engine_instance import ManualEngine
from engine_parts.facts import *
from interface.widgets import campoTexto, campoOpcao, campoNumero

#Arquivo direcionado a interface da aba de disciplinas

#Parte inicial da interface
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
        ManualEngine.run()

    match(st.session_state.get('carregarPagina')):
        case 'cancelamentoDisciplina':
            cancelamentoDisciplina()
        case 'dispensaDisciplina':
            dispensaDisciplina()
        
        #Dispensas
        case 'dispensaGeral':
            dispensaGeral()
        case 'dispensaPorIdade':
            dispensaPorIdade()
        case 'dispensaPorDeficiencia':
            dispensaPorDeficiencia()
        case 'dispensaPorProle':
            dispensaPorProle()
        case 'dispensaIncapacidade':
            dispensaIncapacidade()
        case 'dispensaPorEmprego':
            dispensaPorEmprego()
        case 'nenhumaDispensa':
            nenhumaDispensa()
        
        #Perguntas
        case 'perguntaIdade':
            perguntaIdade()
        case 'perguntaDeficiencia':
            perguntaDeficiencia()
        case 'perguntaFilho':
            perguntaFilhos()
        case 'perguntaIncapacidadeRelativa':
            perguntaIncapacidadeRelativa()
        case 'perguntaEmprego':
            perguntaEmprego()

#Interface para cancelamento de disciplina
def cancelamentoDisciplina():
    st.write("Em datas pré-estabelecidas, no Calendário Acadêmico, o(a) aluno(a) " +
            "poderá requerer cancelamento de uma ou mais disciplinas. No caso de " +
            "alunos diurnos, só poderão cancelar duas disciplinas do bloco principal.")  
    
    st.info(st.session_state.get('explicacao'))

#Interface para perguntar se a disciplina é ed. física
def dispensaDisciplina():
    resposta = campoOpcao (
        'dispensaEdFisica',
        'A disciplina que você busca dispensa é educação física?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(EdFisica(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(EdFisica(tipo = True))
  
#Interface para dispensa geral (não sendo ed. física)
def dispensaGeral():
    st.write("Para requerer dispensa de disciplina cursada em outra Instituição de " +
                "Ensino Superior ou em curso da UFAPE, o(a) aluno(a) deverá preencher " +
                "o requerimento específico, à disposição nas Coordenações de Curso, " +
                "anexando: Histórico Escolar original (ou declaração de cumprimento da " +
                "disciplina em outra Instituição) e o programa da disciplina cursada, " +
                "conforme calendário acadêmico. " +
                "Em seguida, o aluno deverá formalizar um processo no setor de " +
                "Protocolo da UFAPE e a disciplina foi cursada nesta universidade, não é " +
                "necessário anexar o programa de disciplina. O(a) aluno(a) deverá " +
                "frequentar as aulas até o deferimento de sua solicitação evitando sua " +
                "reprovação por faltas.")
    
    st.info(st.session_state.get('explicacao'))

#Interface de dispensa de ed. fisica por idade
def dispensaPorIdade():
    st.write("Você pode requerir uma **Dispensa Definitiva por idade**, " + 
             "basta anexar uma cópia autenticada da certidão de nascimento e/ou casamento.")
    
    st.info(st.session_state.get('explicacao'))

#Interface de dispensa de ed. fisica por deficiencia
def dispensaPorDeficiencia():
    st.write("Você pode requerir uma **Dispensa Definitiva por Deficiência Física**, " + 
             "basta anexar atestado médico, homologado pelos peritos oficiais de saúde " +
             "que atuam no Departamento de Qualidade de Vida (DQV)")
    
    st.info(st.session_state.get('explicacao'))

#Interface de dispensa de ed. fisica por prole
def dispensaPorProle():
    st.write("Você pode requerir uma **Dispensa Definitiva por Prole**, " + 
             "basta anexar uma cópia autenticada da Certidão de Nascimento do filho.")
    
    st.info(st.session_state.get('explicacao'))

#Interface de dispensa parcial de ed. fisica por incapacidade
def dispensaIncapacidade():
    st.write("Você pode requerir uma **Dispensa Parcial por Incapacidade Física Temporária ou Relativa**, " + 
             "basta anexar um atestado, homologado pelos peritos oficiais de saúde que atuam no DQV.")
    
    st.info(st.session_state.get('explicacao'))

#Interface de dispensa parcial de ed. fisica por ter emprego (6h+/dia)
def dispensaPorEmprego():
    st.write("Você pode requerir uma **Dispensa Parcial por Trabalho**, " + 
             "basta anexar uma cópia autenticada da CTPS e requerer semestralmente, até a " +
             "conclusão do curso, se trabalhar durante todo o prazo.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para caso nenhuma dispensa seja aplicável
def nenhumaDispensa():
    st.write("Você não pode requerir nenhuma dispensa para a disciplina de Educação Física.")

    st.info(st.session_state.get('explicacao'))    

#Interface para pergunta de idade
def perguntaIdade():
    resposta = campoNumero (
        'perguntaIdade',
        'Qual é a sua idade?',
        0,
        90
    )
    
    if not resposta is None:
        ManualEngine.declare(Idade(valor = resposta))

#Interface para pergunta de deficiencia física
def perguntaDeficiencia():
    resposta = campoOpcao (
        'deficienciaFisica',
        'Você possui alguma deficiência física?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(DeficienciaFisica(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(DeficienciaFisica(tipo = True))

#Interface para pergunta sobre ter filhos
def perguntaFilhos():
    resposta = campoOpcao (
        'mulherFilhos',
        'Você é mulher e tem filho(s)?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(MulherComFilhos(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(MulherComFilhos(tipo = True))

#Interface para pergunta sobre ter alguma incapacidade
def perguntaIncapacidadeRelativa():
    resposta = campoOpcao (
        'incapacRelativa',
        'Você tem alguma incapacidade física temporária ou relativa?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(IncapacidadeRelativa(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(IncapacidadeRelativa(tipo = True))

#Interface para pergunta sobre ter emprego
def perguntaEmprego():
    resposta = campoOpcao (
        'emprego',
        'Você trabalha com jornada maior ou igual a 6h/dia?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(Emprego6h(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(Emprego6h(tipo = True))