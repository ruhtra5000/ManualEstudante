from experta import *
from facts import *

#Motor de inferencia com definição das regras
class Manual(KnowledgeEngine):
    @Rule(EntradaInicial(txt = "matricula"))
    def matriculaPadrao(self):
        print("Também conhecida como Registro Acadêmico, é a vinculação do(a) "+
                "estudante a um curso da Instituição nas datas previstas no Calendário "+
                "Acadêmico disponível no site da UFAPE.")
        #Falta adicionar a explicabilidade 
        self.declare(SubEntrada(matr = True))
    
    @Rule(SubEntrada(matr = True))
    def subMatricula(self):
        subEntrada = input("Deseja perguntar algo mais específico sobre matricula? ")
        self.declare(SubEntrada(txt = subEntrada))
    
    @Rule(SubEntrada(txt = "semestre"))
    def matrSemestral(self):
        print("A matrícula é da responsabilidade do(a) aluno(a) e deve ser " + 
                "renovada semestralmente, obedecendo às datas divulgadas no " + 
                "Calendário Acadêmico disponível no site da UFAPE, para o " + 
                "prosseguimento de estudos, observando-se a sequência estabelecida no " + 
                "currículo, os pré-requisitos e a compatibilidade de horários. Toda a " + 
                "orientação necessária à matrícula pode ser obtida junto à Coordenação " + 
                "do Curso e à Comissão de Orientação e Acompanhamento Acadêmico " + 
                "(COAA) do seu respectivo Curso.")

    @Rule(SubEntrada(txt = "reajuste"))
    def matrReajuste(self):
        print("Para aquele aluno que efetuou a matrícula regular, mas deseja " +
                "permutar ou excluir disciplina(s). A efetivação do reajuste da matrícula " +
                "só ocorre se ainda houver vaga nas disciplinas que ele permutou, " +
                "ficando em fila de espera classificada pelo ranking.") 