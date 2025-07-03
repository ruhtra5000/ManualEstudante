from experta import *

#Arquivo contendo a declaração dos fatos usados

class MatriculaEntrada(Fact): #Entrada inicial
    txt: str

class DisciplinaEntrada(Fact): #Entrada inicial
    txt: str

class CancelamentoEntrada(Fact): #Entrada inicial
    txt: str

class ApoioEstudantilEntrada(Fact): #Entrada inicial
    txt: str

class ColacaoGrauEntrada(Fact): #Entrada inicial
    txt: str

class EstagioEntrada(Fact): #Entrada inicial
    txt: str

class Sexo(Fact): #Simboliza o sexo do usuário
    valor: str

class Idade(Fact): #Idade do usuário
    valor: int

class PeriodosCursados(Fact): #Armazena a qtde de períodos cursados (inclui o atual)
    valor: int

class Trancamentos(Fact): #Qtde de trancamentos
    valor: int

class AnosEvasao(Fact): #Qtde de anos desvinculado da UFAPE
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

class RecursosAdmEntrada(Fact): #Entrada de recursos administrativos
    txt: str

class Nota1(Fact): # Nota da primeira avaliação
    valor: float

class Nota2(Fact): # Nota da segunda avaliação
    valor: float

class ReprovacoesMesmaMateria(Fact): #Se o usuário ja reprovou 4 vezes numa mesma matéria
    tipo: bool

#BOLSAS

class InteresseMonitoria(Fact): #Se o usuário tem interesse no programa de monitoria
    tipo: bool

class InteressePet(Fact): #Se o usuário tem interesse no programa PET
    tipo: bool

class InteresseBia(Fact): #Se o usuário tem interesse no programa BIA
    tipo: bool

class InteressePibid(Fact): #Se o usuário tem interesse no programa PIBID
    tipo: bool

class InteressePibic(Fact): #Se o usuário tem interesse no programa PIBIC
    tipo: bool

class InteressePrp(Fact): #Se o usuário tem interesse no programa PRP
    tipo: bool

class InteresseExtensao(Fact): #Se o usuário tem interesse no programa de extensão
    tipo: bool

#AUXILIO

class InteresseMobilidade(Fact): #Se o usuário tem interesse no programa de mobilidade
    tipo: bool

class InteressePai(Fact): #Se o usuário tem interesse no programa PAI
    tipo: bool

class InteressePad(Fact): #Se o usuário tem interesse no programa PAD
    tipo: bool

class InteresseResidencia(Fact): #Se o usuário tem interesse no programa de residência
    tipo: bool

class InteresseVoltaAoLar(Fact): #Se o usuário tem interesse no programa de volta ao lar
    tipo: bool

class InteressePag(Fact): #Se o usuário tem interesse no programa PAG
    tipo: bool

class InteresseRural(Fact): #Se o usuário tem interesse no programa de rural
    tipo: bool


#APOIO

class InteressePavi(Fact): #Se o usuário tem interesse no programa PAVI
    tipo: bool

class InteresseCultura(Fact): #Se o usuário tem interesse no programa de cultura
    tipo: bool

class InteresseRemt(Fact): #Se o usuário tem interesse no programa REMT
    tipo: bool

class InteresseAcessibilidade(Fact): #Se o usuário tem interesse no programa de acessibilidade
    tipo: bool