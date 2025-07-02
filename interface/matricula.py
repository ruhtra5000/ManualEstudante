import streamlit as st
from engine_parts.engine_instance import ManualEngine
from engine_parts.facts import *
from interface.widgets import campoTexto, campoOpcao, campoNumero

#Arquivo direcionado a interface da aba de matrícula

#Parte inicial da interface
def matriculaInicial():
    st.header("Matrícula")
    st.write("Também conhecida como Registro Acadêmico, é a vinculação do(a) "+
                "estudante a um curso da Instituição nas datas previstas no Calendário "+
                "Acadêmico disponível no site da UFAPE.")
            
    entrada = campoTexto(
        chave="matricula",
        texto_label="Deseja saber algo mais sobre matrícula?",
        texto_placeholder="Ex.: Semestre, Reajuste, Estagio, Aluno Especial, Critica, Trancamento"
    )
    if entrada:
        ManualEngine.declare(MatriculaEntrada(txt=entrada))
        ManualEngine.imprimirFatos()
        ManualEngine.run()

    match(st.session_state.get('carregarPagina')):
        case 'matriculaSemestral':
            matriculaSemestral()
        case 'reajusteMatricula':
            reajusteMatricula()
        case 'matriculaEstagioObrigatorio':
            matriculaEstagioObrigatorio()
        case 'matriculaAlunoEspecial':
            matriculaAlunoEspecial()
        case 'matriculaNaoAlunoEspecial':
            matriculaNaoAlunoEspecial()
        case 'criticaMatricula':
            criticaMatricula()
        case 'trancamentoMatriculaInicioCurso':
            trancamentoMatriculaInicioCurso()
        case 'trancamentoMatriculaMaximoAtingido':
            trancamentoMatriculaMaximoAtingido()
        case 'trancamentoExtemporaneoMatricula':
            trancamentoExtemporaneoMatricula()
        case 'trancamentoMatriculaPadrao':
            trancamentoMatriculaPadrao()
        
        #Perguntas
        case 'perguntaConcluinte':
            perguntaConcluinte()
        case 'perguntaEgresso':
            perguntaEgresso()
        case 'perguntaPeriodoCursado':
            perguntaPeriodoCursado()
        case 'perguntaTrancamentos':
            perguntaTrancamentos()
        case 'perguntaForcaMaior':
            perguntaForcaMaior()

#Interface para matrícula semestral
def matriculaSemestral():
    st.write("A matrícula é da responsabilidade do(a) aluno(a) e deve ser " + 
                "renovada semestralmente, obedecendo às datas divulgadas no " + 
                "Calendário Acadêmico disponível no site da UFAPE, para o " + 
                "prosseguimento de estudos, observando-se a sequência estabelecida no " + 
                "currículo, os pré-requisitos e a compatibilidade de horários. Toda a " + 
                "orientação necessária à matrícula pode ser obtida junto à Coordenação " + 
                "do Curso e à Comissão de Orientação e Acompanhamento Acadêmico " + 
                "(COAA) do seu respectivo Curso.")

    st.info(st.session_state.get('explicacao'))

#Interface para o reajuste de matrícula
def reajusteMatricula():
    st.write("O reajuste de matrícula é para aquele aluno que efetuou a matrícula regular, mas deseja " +
            "permutar ou excluir disciplina(s). A efetivação do reajuste da matrícula " +
            "só ocorre se ainda houver vaga nas disciplinas que ele permutou, " +
            "ficando em fila de espera classificada pelo ranking.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para matrícula na disciplina de Estágio Supervisionado Obrigatório
def matriculaEstagioObrigatorio():
    st.write("A matrícula na disciplina de Estágio Supervisionado Obrigatório (ESO) " +
            "deverá ser realizada no período normal de matrícula, de acordo com o " +
            "Projeto Pedagógico do Curso nas datas previstas no Calendário " +
            "Acadêmico. A matrícula, neste caso, só será confirmada após a entrega " +
            "da documentação na Seção de Estágio.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para matrícula de aluno especial em disciplina isolada
def matriculaAlunoEspecial():
    st.write("Concluintes da UFAPE e egressos podem requerer inscrição em " +
            "até 02 disciplinas isoladas, na forma de Aluno Especial, por dois " +
            "semestres nos Cursos de Graduação da Universidade, qualquer curso, " +
            "com a finalidade de complementar seus estudos. Sua matrícula, " +
            "quando o requerimento for aprovado, fica condicionada à existência de " +
            "vagas nas disciplinas desejadas, após a matrícula dos(as) alunos(as) " +
            "regulares da Universidade, conforme as datas previstas no Calendário " +
            "Acadêmico")
    
    st.info(st.session_state.get('explicacao'))

#Interface para quem não se enquadra como aluno especial
def matriculaNaoAlunoEspecial():
    st.write("A matrícula de Aluno Especial para disciplinas isoladas " +
             "somente é disponibilizada a concluintes da UFAPE e egressos.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para crítica de matrícula
def criticaMatricula():
    st.write("Após o período de matrículas a administração acadêmica efetua a crítica " +
            "da matrícula, confrontando-a com o regime acadêmico ao qual pertence " +
            "o curso e com o sequenciamento do currículo, cancelando disciplinas " +
            "que estejam em desacordo com ambos.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para o trancamento de matrícula para alunos nos dois primeiros perídos
def trancamentoMatriculaInicioCurso():
    st.write("Está estabelecida, a obrigatoriedade de " +
            "alunos ingressos de cursarem os dois primeiros semestres letivos, não " +
            "sendo permitido trancamento. Nesse caso, somente será permitido o " +
            "cancelamento de, no máximo, duas disciplinas em cada um dos dois " +
            "períodos letivos iniciais, nas datas estabelecidas pelo Calendário " +
            "Acadêmico do ano vigente.")

    st.info(st.session_state.get('explicacao'))

#Interface para caso o número de trancamentos máximo tenha sido atingido
def trancamentoMatriculaMaximoAtingido():
    st.write("Você não pode mais trancar o curso, pois o número máximo de trancamento " +
            "é de 04 semestres consecutivos ou alternados. Enquanto estiver com a matrícula " +
            "\"trancada\", o(a) aluno(a) manterá vínculo com a Universidade, " +
            "entretanto será considerado desistente o(a) aluno(a) que não efetuar " +
            "matrícula subsequente ao término do trancamento.")

    st.info(st.session_state.get('explicacao'))

#Interface para o trancamento extemporaneo de matrícula
def trancamentoExtemporaneoMatricula():
    st.write("Você pode solicitar um Trancamento Extemporâneo de Matrícula que " +
            "trata das situações classificadas como de \"força maior\". Caso haja um " +
            "motivo especial para o trancamento, leve a soliticação a coordenação " +
            "do seu curso.\n\nObs.: As solicitações de trancamento " +
            "por motivo de saúde serão deferidas pela PREG se a Junta Médica do " +
            "Departamento de Qualidade de Vida (DQV) indicar que há limitação da " +
            "capacidade de aprendizagem do(a) estudante. Não há abono de faltas para " +
            "esses casos e isso poderá levar à reprovação nas disciplinas em que esteja " +
            "matriculado.")

    st.info(st.session_state.get('explicacao'))

#Interface para o trancamento padrão de matrícula
def trancamentoMatriculaPadrao():
    st.write("Você pode trancar o curso normalmente, caso deseje ou seja necessário.")

    st.info(st.session_state.get('explicacao'))

#Interface para pergunta sobre o aluno ser concluinte 
def perguntaConcluinte():
    resposta = campoOpcao (
        'concluinte',
        'Você é aluno(a) concluinte de algum curso de graduação da UFAPE, isto é, está no último período?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(ConcluinteUfape(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(ConcluinteUfape(tipo = True))

#Interface para pergunta sobre o aluno ser egresso 
def perguntaEgresso():
    resposta = campoOpcao (
        'egresso',
        'Você é egresso de outra instituição?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(Egresso(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(Egresso(tipo = True))

#Interface para pergunta sobre períodos cursados
def perguntaPeriodoCursado():
    st.write("Trancamento de matrícula é a suspensão parcial das atividades acadêmicas (inclusive da contagem " +
            "do prazo para conclusão do curso) por um semestre letivo. O prazo para " +
            "o trancamento de matrícula, em cada período letivo regular, é " +
            "estabelecido no Calendário Acadêmico. O trancamento pode ser feito " +
            "no dia da matrícula, posteriormente, em cada data pré-fixada no " +
            "Calendário Acadêmico, ou extemporaneamente, devidamente justificado.")
    
    resposta = campoNumero (
        'periodoCursado',
        'Quantos períodos você já cursou, contando com o período atual?',
        1,
        16
    )
    
    if not resposta is None:
        ManualEngine.declare(PeriodosCursados(valor = resposta))

#Interface para pergunta sobre trancamentos realizados
def perguntaTrancamentos():
    st.write("Trancamento de matrícula é a suspensão parcial das atividades acadêmicas (inclusive da contagem " +
            "do prazo para conclusão do curso) por um semestre letivo. O prazo para " +
            "o trancamento de matrícula, em cada período letivo regular, é " +
            "estabelecido no Calendário Acadêmico. O trancamento pode ser feito " +
            "no dia da matrícula, posteriormente, em cada data pré-fixada no " +
            "Calendário Acadêmico, ou extemporaneamente, devidamente justificado.")
    
    resposta = campoNumero (
        'trancamentos',
        'Quantos períodos você já trancou? Sejam eles consecutivos ou alternados.',
        0,
        4
    )
    
    if not resposta is None:
        ManualEngine.declare(Trancamentos(valor = resposta))

#Interface para pergunta sobre motivação do trancamento
def perguntaForcaMaior():
    resposta = campoOpcao (
        'forçaMaior',
        'Caso seja necessário trancar o período, você considera sua motivação como algo de \"força maior\"? ' +
        'Como: trabalho, doença, problemas de saúde, serviço militar, etc',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(TrancamentoForcaMaior(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(TrancamentoForcaMaior(tipo = True))