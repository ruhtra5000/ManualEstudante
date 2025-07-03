from experta import *

#Arquivo contendo a declaração dos fatos usados

class MatriculaEntrada(Fact): #Entrada inicial
    txt: str

class DisciplinaEntrada(Fact): #Entrada inicial
    txt: str

class CancelamentoEntrada(Fact): #Entrada inicial
    txt: str

class Sexo(Fact): #Simboliza o sexo do usuário
    valor: str

class Idade(Fact): #Idade do usuário
    valor: int

class PeriodosCursados(Fact): #Armazena a qtde de períodos cursados (inclui o atual)
    valor: int

class Trancamentos(Fact): #Qtde de trancamentos
    valor: int

class EdFisica(Fact): #Sinaliza se a disciplina que quer dispensar é Ed. Física
    tipo: bool

class DeficienciaFisica(Fact): #Se o usuário tem alguma deficiencia fisica
    tipo: bool

class IncapacidadeRelativa(Fact): #Se o usuário tem uma incapacidade relativa ou temporaria
    tipo: bool

class MulherComFilhos(Fact): #Se o usuário é mulher e tem filho(s)
    tipo: bool

class Emprego6h(Fact): #Se o usuário trabalha com jornada de 6h+/dia
    tipo: bool

class ConcluinteUfape(Fact): #Se o usuário é concluinte da UFAPE
    tipo: bool

class Egresso(Fact): #Se o usuário é egresso de outra instituição
    tipo: bool

class TrancamentoForcaMaior(Fact): #Sinaliza se o motivo de trancamento de matricula
    tipo: bool                     #pode ser categorizado como de "força maior"

class TempoRestanteCurso(Fact): #Se o usuário é capaz de finalizar o curso
    tipo: bool                  #no tempo restante

class AvaliacaoEntrada(Fact): #Entrada de revisão de prova
    txt: str

class PrazoRevisaoOK(Fact): #Se o prazo de revisão de prova está ok
    tipo: bool

class FaltasAbonosEntrada(Fact): #Entrada de faltas e abonos
    txt: str

class ExercicioMilitar(Fact): #Se o usuário está em exercício militar
    tipo: bool

class Gestante(Fact): #Se o usuário é gestante
    tipo: bool
