import streamlit as st
from engine_parts.engine_instance import ManualEngine
from engine_parts.facts import *
from interface.widgets import campoTexto

def estagio():
    st.header("Estágio")
    st.write(
        "O estágio é uma etapa essencial na formação do(a) estudante de graduação, promovendo a aplicação prática dos conhecimentos adquiridos no curso. " +
        "Para realização do estágio, é necessário firmar um Termo de Compromisso entre o(a) estudante, a instituição concedente e a UFAPE, " +
        "com supervisão de um professor orientador e um supervisor na empresa. \n\n" +
        "A UFAPE possui um setor de estágios que orienta e acompanha os trâmites legais, bem como a documentação necessária, como plano de atividades e relatórios. " +
        "Antes de iniciar o estágio, o(a) aluno(a) deve verificar os critérios específicos junto à coordenação do curso."
    )

    entrada = campoTexto(
        chave="estagio",
        texto_label="Deseja saber algo mais sobre estágio?",
        texto_placeholder="Ex.: estágio obrigatório, documentos, etc.."
    )

    if entrada:
        ManualEngine.declare(EstagioEntrada(txt=entrada))
        ManualEngine.imprimirFatos()
