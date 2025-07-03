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
        txt += f"Premissas: {premissas_formatadas}\n\n"
        txt += f"Fonte: {expl['fonte']}"

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


    #                      _ _            /\/|                    _   _       _            
    #       /\            | (_)          |/\/                    | \ | |     | |           
    #      /  \__   ____ _| |_  __ _  ___ ___   ___  ___    ___  |  \| | ___ | |_ __ _ ___ 
    #     / /\ \ \ / / _` | | |/ _` |/ __/ _ \ / _ \/ __|  / _ \ | . ` |/ _ \| __/ _` / __|
    #    / ____ \ V / (_| | | | (_| | (_| (_) |  __/\__ \ |  __/ | |\  | (_) | || (_| \__ \
    #   /_/    \_\_/ \__,_|_|_|\__,_|\___\___/ \___||___/  \___| |_| \_|\___/ \__\__,_|___/
    #                                 )_)                                                  
    #                                                                                      

    # Regra de página inicial para a aba "Avaliações e Notas"
    @Rule(AvaliacaoEntrada(txt = "revisão"))
    def revisaoProva(self):
        st.session_state['carregarPagina'] = 'revisaoProva'

    # Regra para verificar se o prazo de revisão está OK
    @Rule(
        AvaliacaoEntrada(txt = "revisão"),
        PrazoRevisaoOK(tipo = True)
    )
    def revisaoPrazoOK(self):
        st.session_state['carregarPagina'] = 'revisaoPrazoOK'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'revisaoProva',
            'premissas': ['Aba avaliações e notas', 'Busca por \"revisão\"','Prazo de revisão OK'],
            'fonte': 'Pág. 28 do Manual do Estudante 2023',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    # Regra para verificar se o prazo de revisão expirou
    @Rule(
        AvaliacaoEntrada(txt = "revisão"),
        PrazoRevisaoOK(tipo = False)
    )
    def revisaoPrazoExpirado(self):
        st.session_state['carregarPagina'] = 'revisaoPrazoExpirado'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'revisaoPrazoExpirado',
            'premissas': ['Aba avaliações e notas', 'Busca por \"revisão\"','Prazo de revisão expirado'],
            'fonte': 'Pág. 28 do Manual do Estudante 2023',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    # NOVA REGRA: Inicia o fluxo de verificação de notas para cálculo de média/exame final
    @Rule(AS.av_entrada << AvaliacaoEntrada(txt = L("notas") | L("média") | L("media") | L("exame final") | L("exame")))
    def iniciarVerificacaoNotas(self, av_entrada):
        st.session_state['carregarPagina'] = 'perguntarNotas'
        # Reseta flags de notas para iniciar um novo cálculo
        st.session_state['nota1_informada'] = False
        st.session_state['nota2_informada'] = False

        self.explicacao.append({
            'nome': 'iniciarVerificacaoNotas',
            'premissas': ['Aba Avaliações e Notas', 'Busca por \'notas\', \'média\' ou \'exame\''],
            'fonte': 'Pág. 27-28 do Manual do Estudante 2023',
            'tempo': len(self.explicacao) + 1
        })
        self.gerarExplicacao()
        self.retract(av_entrada) # Retrai a entrada inicial para não disparar novamente

    # NOVA REGRA: Calcula a média e determina a situação do aluno
    @Rule(
        AS.n1 << Nota1(valor=P(lambda x: True)), # Nota1 está presente
        AS.n2 << Nota2(valor=P(lambda x: True))  # Nota2 está presente
    )
    def avaliarAprovacao(self, n1, n2):
        media = (n1['valor'] + n2['valor']) / 2.0
        
        st.session_state['carregarPagina'] = 'exibirResultadoFinal' # Indica a UI a ser exibida

        mensagem_resultado = ""
        fonte_explicacao = 'Pág. 27-28 do Manual do Estudante 2023'

        if media >= 7.0:
            mensagem_resultado = f"Sua média é {media:.2f}. Você está **APROVADO(A) POR MÉDIA!**"
            st.success(mensagem_resultado)
            premissas_explicacao = ['Nota1 e Nota2 informadas', f'Média ({media:.2f}) >= 7.0']
        elif media >= 3.0: # media < 7.0 && media >= 3.0
            mensagem_resultado = f"Sua média é {media:.2f}. Você está **ELEGÍVEL PARA EXAME FINAL!** Você será aprovado(a) se obtiver média 5.0 (considerando a média das provas e a nota do exame final)."
            st.warning(mensagem_resultado)
            premissas_explicacao = ['Nota1 e Nota2 informadas', f'Média ({media:.2f}) >= 3.0 e < 7.0']
        else: # media < 3.0
            mensagem_resultado = f"Sua média é {media:.2f}. Você está **REPROVADO(A) SEM DIREITO A EXAME FINAL.**"
            st.error(mensagem_resultado)
            premissas_explicacao = ['Nota1 e Nota2 informadas', f'Média ({media:.2f}) < 3.0']

        self.explicacao.append({
            'nome': 'avaliarAprovacao',
            'premissas': premissas_explicacao,
            'fonte': fonte_explicacao,
            'tempo': len(self.explicacao) + 1
        })
        self.gerarExplicacao()

        # Retrai as notas após o cálculo para limpar a base de conhecimento
        # e permitir um novo cálculo se o usuário informar novas notas.
        self.retract(n1)
        self.retract(n2)
        # Opcional: Resetar as flags de session_state aqui também para garantir
        # que a UI se reinicie para novas entradas de notas.
        st.session_state['nota1_informada'] = False
        st.session_state['nota2_informada'] = False
        
    #    ______    _ _                              _                           
    #   |  ____|  | | |                       /\   | |                          
    #   | |__ __ _| | |_ __ _ ___    ___     /  \  | |__   ___  _ __   ___  ___ 
    #   |  __/ _` | | __/ _` / __|  / _ \   / /\ \ | '_ \ / _ \| '_ \ / _ \/ __|
    #   | | | (_| | | || (_| \__ \ |  __/  / ____ \| |_) | (_) | | | | (_) \__ \
    #   |_|  \__,_|_|\__\__,_|___/  \___| /_/    \_\_.__/ \___/|_| |_|\___/|___/
    #                                                                           
                                                             
    # Caso de busca por "abono"
    # e pergunta se o usuário está sob exercício militar
    @Rule(FaltasAbonosEntrada(txt = 'abono'))
    def abono(self):
        st.session_state['carregarPagina'] = 'abono'
        
    # Caso o aluno esteja sob exercício militar
    @Rule(
        FaltasAbonosEntrada(txt = 'abono'),
        ExercicioMilitar(tipo = True)
    )
    def abonoExercicioMilitar(self):
        st.session_state['carregarPagina'] = 'abonoExercicioMilitar'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'abonoExercicioMilitar',
            'premissas': ['Aba faltas e abonos', 'Busca por \"abono\"', 'Está sob exercício militar'],
            'fonte': 'Pág. 29 do Manual do Estudante 2023. Lei nº 4.375/64',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    # Regra caso o aluno não esteja sob exercício militar
    @Rule(
        FaltasAbonosEntrada(txt = 'abono'),
        ExercicioMilitar(tipo = False)
    )
    def abonoInvalido(self):
        st.session_state['carregarPagina'] = 'abonoInvalido'
        
        self.explicacao.append({   
            'nome': 'abonoInvalido',
            'premissas': ['Aba faltas e abonos', 'Busca por \"abono\"', 'Não está sob exercício militar'],
            'fonte': 'Pág. 29 do Manual do Estudante 2023. Lei nº 4.375/64',
            'Resolulção': '',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    # Caso de busca por "faltas"
    # e pergunta se o usuário é gestante
    @Rule(FaltasAbonosEntrada(txt = 'faltas'))
    def faltas(self):
        st.session_state['carregarPagina'] = 'faltas'

    # Tratamento de faltas caso o usuário gestante
    @Rule(
        FaltasAbonosEntrada(txt = 'faltas'),
        Gestante(tipo = True)
    )
    def tratamentoGestante(self):
        st.session_state['carregarPagina'] = 'tratamentoGestante'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'tratamentoGestante',
            'premissas': ['Aba faltas e abonos', 'Busca por \"faltas\"', 'É gestante'],
            'fonte': 'Pág. 28 do Manual do Estudante 2023. LEI Nº 6202/75.',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    # Tratamento de faltas caso o usuário tenha incapacidade relativa
    @Rule(
        FaltasAbonosEntrada(txt = 'faltas'),
        Gestante(tipo = False),
        IncapacidadeRelativa(tipo = True)
        )
    def tratamentoIncapacitadoRelativo(self):
        st.session_state['carregarPagina'] = 'tratamentoIncapacitadoRelativo'

        self.explicacao.append({
            'nome': 'tratamentoIncapacitadoRelativo',
            'premissas': ['Aba faltas e abonos', 'Busca por \"faltas\"', 'Não é gestante', 'Tem incapacidade relativa'],
            'fonte': 'Pág. 28 do Manual do Estudante 2023. DECRETO-LEI Nº 1044/69.',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    # Pergunta se o usuário tem alguma incapacidade relativa ou temporária    
    @Rule(
        FaltasAbonosEntrada(txt = 'faltas'),
        Gestante(tipo = False)
    )
    def perguntaIncapacidadeRelativa(self):
        st.session_state['carregarPagina'] = 'perguntaIncapacidadeRelativa'

    # Tratamento caso o usuário não seja gestante nem incapacitado relativo
    @Rule(
        FaltasAbonosEntrada(txt = 'faltas'),
        Gestante(tipo = False),
        IncapacidadeRelativa(tipo = False)
    )
    def nenhumTratamentoFaltas(self):
        st.session_state['carregarPagina'] = 'nenhumTratamentoFaltas'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'nenhumTratamentoFaltas',
            'premissas': ['Aba faltas e abonos', 'Busca por \"faltas\"', 'Não é gestante', 'Não tem incapacidade relativa'],
            'fonte': 'Pág. 28 do Manual do Estudante 2023. LEI Nº 6202/75. DECRETO-LEI Nº 1044/69.',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()


#    _____  ______ _____ _    _ _____   _____  ____   _____            _____  __  __ 
#   |  __ \|  ____/ ____| |  | |  __ \ / ____|/ __ \ / ____|     /\   |  __ \|  \/  |
#   | |__) | |__ | |    | |  | | |__) | (___ | |  | | (___      /  \  | |  | | \  / |
#   |  _  /|  __|| |    | |  | |  _  / \___ \| |  | |\___ \    / /\ \ | |  | | |\/| |
#   | | \ \| |___| |____| |__| | | \ \ ____) | |__| |____) |  / ____ \| |__| | |  | |
#   |_|  \_\______\_____|\____/|_|  \_\_____/ \____/|_____/  /_/    \_\_____/|_|  |_|
#                                                                                                                                                                       

    @Rule(RecursosAdmEntrada(txt = "reapreciação"))
    def reapreciacao(self):
        st.session_state['carregarPagina'] = 'reapreciação'

        self.explicacao.append({
            'nome': 'reapreciacao',
            'premissas': ['Aba recursos administrativos', 'Busca por \"reapreciação\"'],
            'fonte': 'Pág. 30 do Manual do Estudante 2023',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    @Rule(RecursosAdmEntrada(txt = "recurso"))
    def recurso(self):
        st.session_state['carregarPagina'] = 'recurso'

        self.explicacao.append({
            'nome': 'recurso',
            'premissas': ['Aba recursos administrativos', 'Busca por \"recurso\"'],
            'fonte': 'Pág. 30 do Manual do Estudante 2023',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()
