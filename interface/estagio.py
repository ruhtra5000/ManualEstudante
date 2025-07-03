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
        texto_placeholder="Ex.: Estágio obrigatório, Estágio não obrigatório, Requisitos"
    )

    if entrada:
        ManualEngine.declare(EstagioEntrada(txt=entrada))
        ManualEngine.imprimirFatos()
        ManualEngine.run()

    match(st.session_state.get('carregarPagina')):
        case 'estagioObrigatorio':
            estagioObrigatorio()
        case 'estagioNaoObrigatorio':
            estagioNaoObrigatorio()
        case 'estagioRequisitos':
            estagioRequisitos()

#Interface para estágio obrigatório
def estagioObrigatorio():
    st.write("O Estágio Supervisionado Obrigatório - é definido no Projeto do Curso, " +
            "cuja carga horária é requisito para aprovação e obtenção do diploma.")

    st.info(st.session_state.get('explicacao'))

#Interface para estágio não obrigatório
def estagioNaoObrigatorio():
    st.write("O Estágio Supervisionado Não-Obrigatório - constui-se em atividade " +
            "complementar à formação acadêmico-profissional do(a) aluno(a), " +
            "realizada por livre escolha do mesmo, dentro de sua área de formação, " +
            "desenvolvido como atividade opcional.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para eos requesitos de um estágio
def estagioRequisitos():
    st.write("O estágio tem como requisitos: " +
            "\n\n• Matrícula e frequência regular. " +
            "\n\n• Celebração de Termo de Compromisso, entre o(a) estudante, a unidade concedente e a instituição de ensino. " +
            "\n\n• Compatibilidade entre as atividades desenvolvidas no estágio e aquelas previstas no Termo de Compromisso. ")
    
    st.info(st.session_state.get('explicacao'))