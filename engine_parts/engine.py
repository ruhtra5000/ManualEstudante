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

        txt = '**Explicação:**\n\n'
        txt += f"Premissas: {expl['premissas']}\n\n"
        txt += f"Fonte: {expl['fonte']}"

        st.session_state['explicacao'] = txt

    #Função que imprime os fatos (debug)
    def imprimirFatos(self):
        print("\nFatos atuais:")
        print(self.facts)

    #Regras
    #Matricula
    @Rule(MatriculaEntrada(txt = "semestre"))
    def matrSemestral(self):
        st.write("A matrícula é da responsabilidade do(a) aluno(a) e deve ser " + 
                "renovada semestralmente, obedecendo às datas divulgadas no " + 
                "Calendário Acadêmico disponível no site da UFAPE, para o " + 
                "prosseguimento de estudos, observando-se a sequência estabelecida no " + 
                "currículo, os pré-requisitos e a compatibilidade de horários. Toda a " + 
                "orientação necessária à matrícula pode ser obtida junto à Coordenação " + 
                "do Curso e à Comissão de Orientação e Acompanhamento Acadêmico " + 
                "(COAA) do seu respectivo Curso.")

    @Rule(MatriculaEntrada(txt = "reajuste"))
    def matrReajuste(self):
        st.write("Para aquele aluno que efetuou a matrícula regular, mas deseja " +
                "permutar ou excluir disciplina(s). A efetivação do reajuste da matrícula " +
                "só ocorre se ainda houver vaga nas disciplinas que ele permutou, " +
                "ficando em fila de espera classificada pelo ranking.")
    

    #Disciplina
    @Rule(DisciplinaEntrada(txt = "cancelamento"))
    def cancelamentoDisciplina(self):
        st.session_state['carregarPagina'] = 'cancelamentoDisciplina'

        #Explicabilidade
        self.explicacao.append({
            'nome': 'cancelamentoDisciplina',
            'premissas': ['Aba disciplina', 'Busca por \'cancelamento\''],
            'fonte': 'Pág. 25 do Manual do Estudande 2023',
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
            'premissas': ['Aba disciplina', 'Busca por \'dispensa\'', 'Não é dispensa de educação física'],
            'fonte': 'Pág. 25 do Manual do Estudande 2023, e Resolução Nº 442/2006 CEPE/UFRPE',
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
            'premissas': ['Aba disciplina', 'Busca por \'dispensa\'', 'Dispensa ed. física', 'Maior de 30 anos de idade'],
            'fonte': 'Pág. 25 do Manual do Estudande 2023, e Resolução Nº 442/2006 CEPE/UFRPE',
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
            'premissas': ['Aba disciplina', 'Busca por \'dispensa\'', 'Dispensa ed. física', 'Tem deficiencia física'],
            'fonte': 'Pág. 25 do Manual do Estudande 2023, e Resolução Nº 442/2006 CEPE/UFRPE',
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
            'premissas': ['Aba disciplina', 'Busca por \'dispensa\'', 'Dispensa ed. física', 'Mulher com filho(s)'],
            'fonte': 'Pág. 26 do Manual do Estudande 2023, e Resolução Nº 442/2006 CEPE/UFRPE',
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
            'premissas': ['Aba disciplina', 'Busca por \'dispensa\'', 'Dispensa ed. física', 'Tem alguma incapacidade fisica temporaria ou relativa'],
            'fonte': 'Pág. 26 do Manual do Estudande 2023, e Resolução Nº 442/2006 CEPE/UFRPE',
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
            'premissas': ['Aba disciplina', 'Busca por \'dispensa\'', 'Dispensa ed. física', 'Trabalha com jornada maior ou igual a 6h'],
            'fonte': 'Pág. 26 do Manual do Estudande 2023, e Resolução Nº 442/2006 CEPE/UFRPE',
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
            'premissas': ['Aba disciplina', 'Busca por \'dispensa\'', 'Dispensa ed. física', 'Tem menos de 30 anos', 
                          'Não tem deficiência física', 'Não tem filhos ou é mulher', 'Não tem incapacidade relativa ou temporal',
                          'Não trabalha com jornada maior ou igual a 6h/dia'],
            'fonte': 'Pág. 25-26 do Manual do Estudande 2023, e Resolução Nº 442/2006 CEPE/UFRPE',
            'tempo': len(self.explicacao) + 1
        })

        self.gerarExplicacao()

    #Cancelamento de vínculo
    @Rule(CancelamentoEntrada(txt = "lorem ipsum"))
    def cancelPadrao(self):
        '''st.header("Cancelamento de vínculo")
        st.write("O cancelamento de registro acadêmico é o desligamento efetivo da UFAPE.")'''
        #Falta adicionar a explicabilidade 