from experta import *
from engine_parts.facts import *
import streamlit as st

#Motor de inferencia com definição das regras
class Manual(KnowledgeEngine):

    #Construtor
    def __init__(self):
        super().__init__()
        self.explicacao = [] #Armazena a explicabilidade

    #Função que gera explicabilidade em texto
    def gerarExplicacao(self):
        expl = self.explicacao[-1] 

        #Junta as premissas em uma string separada por vírgulas
        premissas_formatadas = ', '.join(expl["premissas"])

        txt = '**Explicação:**\n\n'
        txt += f'Premissas: {premissas_formatadas}\n\n'
        txt += f'Fonte: {expl['fonte']}'

        st.session_state['explicacao'] = txt

    #Função que imprime os fatos (debug)
    def imprimirFatos(self):
        print("\nFatos atuais:")
        print(self.facts)

    #Regras
    #    __  __       _        _            _       
    #   |  \/  |     | |      (_)          | |      
    #   | \  / | __ _| |_ _ __ _  ___ _   _| | __ _ 
    #   | |\/| |/ _` | __| '__| |/ __| | | | |/ _` |
    #   | |  | | (_| | |_| |  | | (__| |_| | | (_| |
    #   |_|  |_|\__,_|\__|_|  |_|\___|\__,_|_|\__,_|
    #                                       
    @Rule(MatriculaEntrada(txt = "semestre"))
    def matriculaSemestral(self):
        st.session_state['carregarPagina'] = 'matriculaSemestral'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'matriculaSemestral',
            'premissas': ['Aba matricula', 'Busca por \"semestre\"'],
            'fonte': 'Pág. 22 do Manual do Estudante 2023',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()
        
    @Rule(MatriculaEntrada(txt = "reajuste"))
    def reajusteMatricula(self):
        st.session_state['carregarPagina'] = 'reajusteMatricula'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'reajusteMatricula',
            'premissas': ['Aba matricula', 'Busca por \"reajuste\"'],
            'fonte': 'Pág. 22-23 do Manual do Estudante 2023',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()
    
    @Rule(MatriculaEntrada(txt = "estagio"))
    def matriculaEstagioObrigatorio(self):
        st.session_state['carregarPagina'] = 'matriculaEstagioObrigatorio'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'matriculaEstagioObrigatorio',
            'premissas': ['Aba matricula', 'Busca por \"estagio\"'],
            'fonte': 'Pág. 23 do Manual do Estudante 2023',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()
    
    @Rule(MatriculaEntrada(txt = "aluno especial"))
    def matriculaAlunoEspecialPergunta1(self):
        st.session_state['carregarPagina'] = 'perguntaConcluinte'

    @Rule(
        MatriculaEntrada(txt = "aluno especial"),
        ConcluinteUfape(tipo = False)
    )
    def matriculaAlunoEspecialPergunta2(self):
        st.session_state['carregarPagina'] = 'perguntaEgresso'

    @Rule(
        MatriculaEntrada(txt = "aluno especial"),
        OR(
            ConcluinteUfape(tipo = True), 
            Egresso(tipo = True)
        )
    )
    def matriculaAlunoEspecial(self):
        st.session_state['carregarPagina'] = 'matriculaAlunoEspecial'
        
        #Explicabilidade
        self.explicacao.append({
            'nome': 'matriculaAlunoEspecial',
            'premissas': ['Aba matricula', 'Busca por \"aluno especial\"', 'É concluinte da UFAPE ou egresso'],
            'fonte': 'Pág. 23 do Manual do Estudante 2023',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()
    
    @Rule(
        MatriculaEntrada(txt = "aluno especial"),
        ConcluinteUfape(tipo = False), 
        Egresso(tipo = False)
    )
    def matriculaNaoAlunoEspecial(self):
        st.session_state['carregarPagina'] = 'matriculaNaoAlunoEspecial'
        
        #Explicabilidade
        self.explicacao.append({
            'nome': 'matriculaNaoAlunoEspecial',
            'premissas': ['Aba matricula', 'Busca por \"aluno especial\"', 'Não é concluinte da UFAPE nem egresso'],
            'fonte': 'Pág. 23 do Manual do Estudante 2023',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    @Rule(MatriculaEntrada(txt = "critica"))
    def criticaMatricula(self):
        st.session_state['carregarPagina'] = 'criticaMatricula'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'criticaMatricula',
            'premissas': ['Aba matricula', 'Busca por \"critica\"'],
            'fonte': 'Pág. 23 do Manual do Estudante 2023',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    @Rule(MatriculaEntrada(txt = "trancamento"))
    def trancamentoMatriculaPergunta1(self):
        st.session_state['carregarPagina'] = 'perguntaPeriodoCursado'

    @Rule(
        MatriculaEntrada(txt = "trancamento"),
        PeriodosCursados(valor = P(lambda v: v <= 2))
    )
    def trancamentoMatriculaInicioCurso(self):
        st.session_state['carregarPagina'] = 'trancamentoMatriculaInicioCurso'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'trancamentoMatriculaInicioCurso',
            'premissas': ['Aba matricula', 'Busca por \"trancamento\"', 'Está cursando o primeiro ou segundo período'],
            'fonte': 'Pág. 24 do Manual do Estudante 2023, e Resolução Nº 486/2006 CEPE/UFRPE',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    @Rule(
        MatriculaEntrada(txt = "trancamento"),
        PeriodosCursados(valor = P(lambda v: v > 2))
    )
    def trancamentoMatriculaPergunta2(self):
        st.session_state['carregarPagina'] = 'perguntaTrancamentos'

    @Rule(
        MatriculaEntrada(txt = "trancamento"),
        Trancamentos(valor = 4)
    )
    def trancamentoMatriculaMaximoAtingido(self):
        st.session_state['carregarPagina'] = 'trancamentoMatriculaMaximoAtingido'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'trancamentoMatriculaMaximoAtingido',
            'premissas': ['Aba matricula', 'Busca por \"trancamento\"', 'Já trancou o curso quatro vezes'],
            'fonte': 'Pág. 24 do Manual do Estudante 2023',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    @Rule(
        MatriculaEntrada(txt = "trancamento"),
        Trancamentos(valor = P(lambda v: v < 4))
    )
    def trancamentoMatriculaPergunta3(self):
        st.session_state['carregarPagina'] = 'perguntaForcaMaior'

    @Rule(
        MatriculaEntrada(txt = "trancamento"),
        TrancamentoForcaMaior(tipo = True)
    )
    def trancamentoExtemporaneoMatricula(self):
        st.session_state['carregarPagina'] = 'trancamentoExtemporaneoMatricula'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'trancamentoExtemporaneoMatricula',
            'premissas': ['Aba matricula', 'Busca por \"trancamento\"', 'Motivo de força maior para o trancamento do curso'],
            'fonte': 'Pág. 24 do Manual do Estudante 2023, Resolução Nº 298/2003 CEPE/UFRPE',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    @Rule(
        MatriculaEntrada(txt = "trancamento"),
        PeriodosCursados(valor = P(lambda v: v > 2)),
        Trancamentos(valor = P(lambda v: v < 4)),
        TrancamentoForcaMaior(tipo = False)
    )
    def trancamentoMatriculaPadrao(self):
        st.session_state['carregarPagina'] = 'trancamentoMatriculaPadrao'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'trancamentoMatriculaPadrao',
            'premissas': ['Aba matricula', 'Busca por \"trancamento\"', 'Cursou mais que dois períodos', 
                          'Trancou menos que quatro vezes', 'Não tem motivo de força maior para o trancamento'],
            'fonte': 'Pág. 23-25 do Manual do Estudante 2023',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()


    #    _____  _          _       _ _             
    #   |  __ \(_)        (_)     | (_)            
    #   | |  | |_ ___  ___ _ _ __ | |_ _ __   __ _ 
    #   | |  | | / __|/ __| | '_ \| | | '_ \ / _` |
    #   | |__| | \__ \ (__| | |_) | | | | | | (_| |
    #   |_____/|_|___/\___|_| .__/|_|_|_| |_|\__,_|
    #                       | |                    
    #                       |_|                    
    #
    @Rule(DisciplinaEntrada(txt = "cancelamento"))
    def cancelamentoDisciplina(self):
        st.session_state['carregarPagina'] = 'cancelamentoDisciplina'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'cancelamentoDisciplina',
            'premissas': ['Aba disciplina', 'Busca por \"cancelamento\"'],
            'fonte': 'Pág. 25 do Manual do Estudante 2023',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()
    
    @Rule(DisciplinaEntrada(txt = "dispensa"))
    def dispensaDisciplina(self):
        st.session_state['carregarPagina'] = 'dispensaDisciplina'

    @Rule(
        DisciplinaEntrada(txt = "dispensa"),
        EdFisica(tipo = False)
    )
    def dispensaGeral(self):
        st.session_state['carregarPagina'] = 'dispensaGeral'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'dispensaGeral',
            'premissas': ['Aba disciplina', 'Busca por \"dispensa\"', 'Não é dispensa de educação física'],
            'fonte': 'Pág. 25 do Manual do Estudante 2023, e Resolução Nº 442/2006 CEPE/UFRPE',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()
    
    @Rule(
        DisciplinaEntrada(txt = "dispensa"), 
        EdFisica(tipo = True)
    )
    def dispensaEdFisicaPergunta1(self):
        st.session_state['carregarPagina'] = 'perguntaIdade'

    @Rule(
        DisciplinaEntrada(txt = "dispensa"), 
        EdFisica(tipo = True), 
        Idade(valor=P(lambda v: v >= 30))
    )
    def dispensaPorIdade(self):
        st.session_state['carregarPagina'] = 'dispensaPorIdade'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'dispensaPorIdade',
            'premissas': ['Aba disciplina', 'Busca por \"dispensa\"', 'Dispensa ed. física', 'Maior de 30 anos de idade'],
            'fonte': 'Pág. 25 do Manual do Estudante 2023, e Resolução Nº 442/2006 CEPE/UFRPE',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    @Rule(
        DisciplinaEntrada(txt = "dispensa"), 
        EdFisica(tipo = True), 
        Idade(valor=P(lambda v: v < 30))
    )
    def dispensaEdFisicaPergunta2(self):
        st.session_state['carregarPagina'] = 'perguntaDeficiencia'

    @Rule(
        DisciplinaEntrada(txt = "dispensa"), 
        EdFisica(tipo = True), 
        DeficienciaFisica(tipo = True)
    )
    def dispensaPorDeficiencia(self):
        st.session_state['carregarPagina'] = 'dispensaPorDeficiencia'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'dispensaPorDeficiencia',
            'premissas': ['Aba disciplina', 'Busca por \"dispensa\"', 'Dispensa ed. física', 'Tem deficiencia física'],
            'fonte': 'Pág. 25 do Manual do Estudante 2023, e Resolução Nº 442/2006 CEPE/UFRPE',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    @Rule(
        DisciplinaEntrada(txt = "dispensa"), 
        EdFisica(tipo = True), 
        DeficienciaFisica(tipo = False)
    )
    def dispensaEdFisicaPergunta3(self):
        st.session_state['carregarPagina'] = 'perguntaFilho'

    @Rule(
        DisciplinaEntrada(txt = "dispensa"), 
        EdFisica(tipo = True), 
        MulherComFilhos(tipo = True)
    )
    def dispensaPorProle(self):
        st.session_state['carregarPagina'] = 'dispensaPorProle'

        self.declare(Sexo(valor = 'feminino'))

        #Explicabilidade
        self.explicacao.append({
            'nome': 'dispensaPorProle',
            'premissas': ['Aba disciplina', 'Busca por \"dispensa\"', 'Dispensa ed. física', 'Mulher com filho(s)'],
            'fonte': 'Pág. 26 do Manual do Estudante 2023, e Resolução Nº 442/2006 CEPE/UFRPE',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    @Rule(
        DisciplinaEntrada(txt = "dispensa"), 
        EdFisica(tipo = True), 
        MulherComFilhos(tipo = False)
    )
    def dispensaEdFisicaPergunta4(self):
        st.session_state['carregarPagina'] = 'perguntaIncapacidadeRelativa'

    @Rule(
        DisciplinaEntrada(txt = "dispensa"), 
        EdFisica(tipo = True), 
        IncapacidadeRelativa(tipo = True)
    )
    def dispensaIncapacidade(self):
        st.session_state['carregarPagina'] = 'dispensaIncapacidade'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'dispensaIncapacidade',
            'premissas': ['Aba disciplina', 'Busca por \"dispensa\"', 'Dispensa ed. física', 'Tem alguma incapacidade fisica temporaria ou relativa'],
            'fonte': 'Pág. 26 do Manual do Estudante 2023, e Resolução Nº 442/2006 CEPE/UFRPE',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()
    
    @Rule(
        DisciplinaEntrada(txt = "dispensa"), 
        EdFisica(tipo = True), 
        IncapacidadeRelativa(tipo = False)
    )
    def dispensaEdFisicaPergunta5(self):
        st.session_state['carregarPagina'] = 'perguntaEmprego'

    @Rule(
        DisciplinaEntrada(txt = "dispensa"), 
        EdFisica(tipo = True), 
        Emprego6h(tipo = True)
    )
    def dispensaPorEmprego(self):
        st.session_state['carregarPagina'] = 'dispensaPorEmprego'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'dispensaPorEmprego',
            'premissas': ['Aba disciplina', 'Busca por \"dispensa\"', 'Dispensa ed. física', 'Trabalha com jornada maior ou igual a 6h'],
            'fonte': 'Pág. 26 do Manual do Estudante 2023, e Resolução Nº 442/2006 CEPE/UFRPE',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    @Rule(
        DisciplinaEntrada(txt = "dispensa"), 
        EdFisica(tipo = True),
        Idade(valor=P(lambda v: v < 30)),
        DeficienciaFisica(tipo = False),
        MulherComFilhos(tipo = False),
        IncapacidadeRelativa(tipo = False), 
        Emprego6h(tipo = False)
    )
    def nenhumaDispensa(self):
        st.session_state['carregarPagina'] = 'nenhumaDispensa'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'nenhumaDispensa',
            'premissas': ['Aba disciplina', 'Busca por \"dispensa\"', 'Dispensa ed. física', 'Tem menos de 30 anos', 
                          'Não tem deficiência física', 'Não tem filhos ou é mulher', 'Não tem incapacidade relativa ou temporal',
                          'Não trabalha com jornada maior ou igual a 6h/dia'],
            'fonte': 'Pág. 25-26 do Manual do Estudante 2023, e Resolução Nº 442/2006 CEPE/UFRPE',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    #     _____                     _                            _              _              __                 _       
    #    / ____|                   | |                          | |            | |            /_/                | |      
    #   | |     __ _ _ __   ___ ___| | __ _ _ __ ___   ___ _ __ | |_ ___     __| | ___  __   ___ _ __   ___ _   _| | ___  
    #   | |    / _` | '_ \ / __/ _ \ |/ _` | '_ ` _ \ / _ \ '_ \| __/ _ \   / _` |/ _ \ \ \ / / | '_ \ / __| | | | |/ _ \ 
    #   | |___| (_| | | | | (_|  __/ | (_| | | | | | |  __/ | | | || (_) | | (_| |  __/  \ V /| | | | | (__| |_| | | (_) |
    #    \_____\__,_|_| |_|\___\___|_|\__,_|_| |_| |_|\___|_| |_|\__\___/   \__,_|\___|   \_/ |_|_| |_|\___|\__,_|_|\___/ 
    #                                                                                                                         
    @Rule(CancelamentoEntrada(txt = "lorem ipsum"))
    def cancelPadrao(self):
        '''st.header("Cancelamento de vínculo")
        st.write("O cancelamento de registro acadêmico é o desligamento efetivo da UFAPE.")'''
        #Falta adicionar a explicabilidade 


    #     _____      _            /\/|             _                              
    #    / ____|    | |          |/\/             | |                             
    #   | |     ___ | | __ _  ___ __ _  ___     __| | ___    __ _ _ __ __ _ _   _ 
    #   | |    / _ \| |/ _` |/ __/ _` |/ _ \   / _` |/ _ \  / _` | '__/ _` | | | |
    #   | |___| (_) | | (_| | (_| (_| | (_) | | (_| |  __/ | (_| | | | (_| | |_| |
    #    \_____\___/|_|\__,_|\___\__,_|\___/   \__,_|\___|  \__, |_|  \__,_|\__,_|
    #                         )_)                            __/ |                
    #                                                       |___/    
    @Rule(ColacaoGrauEntrada(txt = "colação em separado"))
    def colacaoEmSeparado(self):
        st.session_state['carregarPagina'] = 'colacaoEmSeparado'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'colacaoEmSeparado',
            'premissas': ['Aba colação de grau', 'Busca por \"colação em separado\"'],
            'fonte': 'Pág. 31 do Manual do Estudante 2023',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    @Rule(ColacaoGrauEntrada(txt = "aluno laureado"))
    def colacaoAlunoLaureado(self):
        st.session_state['carregarPagina'] = 'colacaoAlunoLaureado'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'colacaoAlunoLaureado',
            'premissas': ['Aba colação de grau', 'Busca por \"aluno laureado\"'],
            'fonte': 'Pág. 31 do Manual do Estudante 2023',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    #    ______     _    __        _       
    #   |  ____|   | |  /_/       (_)      
    #   | |__   ___| |_ __ _  __ _ _  ___  
    #   |  __| / __| __/ _` |/ _` | |/ _ \ 
    #   | |____\__ \ || (_| | (_| | | (_) |
    #   |______|___/\__\__,_|\__, |_|\___/ 
    #                         __/ |        
    #                        |___/      
    @Rule(EstagioEntrada(txt = "estágio obrigatório"))
    def estagioObrigatorio(self):
        st.session_state['carregarPagina'] = 'estagioObrigatorio'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'estagioObrigatorio',
            'premissas': ['Aba Estágio', 'Busca por \"estágio obrigatório\"'],
            'fonte': 'Pág. 37 e 38 do Manual do Estudante 2023 e resolução 678/2008-CEPE/UFRPE',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    @Rule(EstagioEntrada(txt = "estágio não obrigatório"))
    def estagioNaoObrigatorio(self):
        st.session_state['carregarPagina'] = 'estagioNaoObrigatorio'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'estagioNaoObrigatorio',
            'premissas': ['Aba Estágio', 'Busca por \"estágio não obrigatório\"'],
            'fonte': 'Pág. 37 e 38 do Manual do Estudante 2023 e resolução 677/2008-CEPE/UFRPE',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    @Rule(EstagioEntrada(txt = "requisitos"))
    def estagioRequisitos(self):
        st.session_state['carregarPagina'] = 'estagioRequisitos'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'estagioRequisitos',
            'premissas': ['Aba Estágio', 'Busca por \"requisitos\"'],
            'fonte': 'Pág. 38 do Manual do Estudante 2023',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()