from experta import *

#Arquivo contendo a declaração dos fatos usados

class MatriculaEntrada(Fact):
    txt: str

class DisciplinaEntrada(Fact):
    txt: str

class CancelamentoEntrada(Fact):
    txt: str

class Sexo(Fact):
    valor: str

class Idade(Fact):
    valor: int

class PeriodosCursados(Fact):
    valor: int

class Trancamentos(Fact):
    valor: int

class EdFisica(Fact):
    tipo: bool

class DeficienciaFisica(Fact):
    tipo: bool

class IncapacidadeRelativa(Fact):
    tipo: bool

class MulherComFilhos(Fact):
    tipo: bool

class Emprego6h(Fact):
    tipo: bool

class ConcluinteUfape(Fact):
    tipo: bool

class Egresso(Fact):
    tipo: bool

class TrancamentoForcaMaior(Fact):
    tipo: bool