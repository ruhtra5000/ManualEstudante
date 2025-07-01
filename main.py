from experta import *
from engine_parts.facts import *
from engine_parts.engine_instance import ManualEngine
from interface.home import homepageInicial

#Arquivo inicial que "limpa" o motor de inferencia
#uma unica vez e renderiza a página inicial com streamlit

ManualEngine.reset()
    
homepageInicial()

