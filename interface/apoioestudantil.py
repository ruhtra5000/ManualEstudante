import streamlit as st
from engine_parts.engine_instance import ManualEngine
from engine_parts.facts import *
from interface.widgets import campoTexto

def apoioEstudantil():
    st.header("Apoio Estudantil")
    st.write(
        "Os programas de apoio aos estudantes de graduação da UFAPE são iniciativas que visam oferecer suporte " +
        "financeiro, psicológico, pedagógico e social para garantir a permanência e o bom desempenho dos estudantes. " +
        "Esses programas incluem auxílios como moradia, alimentação, transporte, material didático, além de ações " +
        "de acompanhamento e orientação estudantil. Para mais informações, consulte o site oficial da UFAPE ou o setor de assistência estudantil.")

    entrada = campoTexto(
        chave="apoio_estudantil",
        texto_label="Deseja saber algo mais sobre apoio estudantil?",
        texto_placeholder="Ex.: moradia, alimentação, monitoria, PET, BIA, PAVI, PIBID, PIBIC, PRP, PAI, PAD, etc.."
    )
    
    if entrada:
        ManualEngine.declare(ApoioEstudantilEntrada(txt=entrada))
        ManualEngine.imprimirFatos()
