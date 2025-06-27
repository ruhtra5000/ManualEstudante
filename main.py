from experta import *
from facts import *
from engine import *

#Inicialização da aplicação, instanciando e 
#rodando o motor de inferência 

engine = Manual()
engine.reset()
engine.declare(EntradaInicial(txt = input("Qual tema deseja pesquisar? ")))

engine.run()
