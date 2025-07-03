import streamlit as st
from engine_parts.engine_instance import ManualEngine
from engine_parts.facts import AvaliacaoEntrada, PrazoRevisaoOK, Nota1, Nota2
from interface.widgets import campoTexto, campoOpcao, campoNumero

# Função inicial da aba "Avaliações e Notas"
def avaliacoesInicial():
    st.header("Avaliações e Notas")
    st.write("Aqui você encontra informações sobre seu rendimento acadêmico, avaliações, e o processo de revisão de notas.")

    # Campo de texto para o usuário digitar a dúvida inicial
    entrada = campoTexto(
        chave="avaliacoes_geral",
        texto_label="Deseja saber algo mais sobre avaliações, notas ou revisão de provas?",
        texto_placeholder="Ex.: revisão, notas"
    )

    if entrada:
        ManualEngine.declare(AvaliacaoEntrada(txt=entrada.lower()))
        ManualEngine.imprimirFatos()

    match st.session_state.get('carregarPagina'):
        # Interfaces principais
        case 'revisaoProva':
            revisaoProva()

        # Casos de revisão
        case 'revisaoPrazoOK':
            revisaoPrazoOK()
        case 'revisaoPrazoExpirado':
            revisaoPrazoExpirado()

        # Casos de notas
        case 'perguntarNotas': # Para iniciar o fluxo de perguntas sobre as notas
            perguntarNotas()
        case 'exibirResultadoFinal': # Para exibir o resultado após as notas
            exibirResultadoFinal()
        

def revisaoProva():
    
    resposta = campoOpcao(
        chave='revisaoProva',
        texto_label='Você está requerindo a revisão da prova dentro dum prazo de 48h após a publicação da mesma?',
        opcoes=['Sim', 'Não']
    )

    if not resposta is None and resposta == 'sim':
        ManualEngine.declare(PrazoRevisaoOK(tipo=True))
    
    elif not resposta is None and resposta == 'não':
        ManualEngine.declare(PrazoRevisaoOK(tipo=False))

def revisaoPrazoOK():
    st.write("Você pode solicitar a revisão da prova! Para isto, entre em contato com o professor responsável pela disciplina.")

    st.info(st.session_state.get('explicacao'))

def revisaoPrazoExpirado():
    st.write("Infelizmente, o prazo para solicitar a revisão da prova já expirou. Você não poderá mais solicitar a revisão.")

    st.info(st.session_state.get('explicacao'))

# Interface para perguntar as notas da 1ª e 2ª VA
def perguntarNotas():
    st.subheader("Verificação de Aprovação por Média")
    st.write("Para calcular sua situação de aprovação, por favor, informe suas notas.")

    # Estado para controlar qual nota estamos pedindo
    if 'nota1_informada' not in st.session_state:
        st.session_state['nota1_informada'] = False
    if 'nota2_informada' not in st.session_state:
        st.session_state['nota2_informada'] = False

    # Pergunta a Nota 1
    if not st.session_state['nota1_informada']:
        entrada_nota1 = campoNumero(
            "nota1_va", # Chave única
            "Digite a nota da primeira avaliação (0 a 10):",
            0.0,
            10.0
        )
        if entrada_nota1 is not None:
            # Retrair Nota1 anterior se existir
            for fact_id, fact in ManualEngine.facts.items():
                if isinstance(fact, Nota1):
                    ManualEngine.retract(fact_id)
            
            ManualEngine.declare(Nota1(valor=float(entrada_nota1)))
            ManualEngine.imprimirFatos()
            st.session_state['nota1_informada'] = True # Marca que a Nota1 foi informada
            # Não mude 'carregarPagina' aqui, deixe o engine decidir o próximo passo (se for pedir Nota2)
            # A engine vai re-executar e a lógica acima vai ver st.session_state['nota1_informada'] = True

    # Pergunta a Nota 2, somente se Nota 1 já foi informada e Nota 2 ainda não
    elif st.session_state['nota1_informada'] and not st.session_state['nota2_informada']:
        entrada_nota2 = campoNumero(
            "nota2_va", # Chave única
            "Digite a nota da segunda avaliação (0 a 10):",
            0.0,
            10.0
        )
        if entrada_nota2 is not None:
            # Retrair Nota2 anterior se existir
            for fact_id, fact in ManualEngine.facts.items():
                if isinstance(fact, Nota2):
                    ManualEngine.retract(fact_id)

            ManualEngine.declare(Nota2(valor=float(entrada_nota2)))
            ManualEngine.imprimirFatos()
            st.session_state['nota2_informada'] = True # Marca que a Nota2 foi informada
            # Não mude 'carregarPagina' aqui. O engine vai re-executar e
            # disparar a regra de cálculo da média.

# Interface para exibir o resultado da elegibilidade para o Exame Final
def exibirResultadoFinal():
    st.subheader("Resultado da Elegibilidade para Exame Final")
    # O conteúdo desta função será definido pelas regras no engine.py,
    # que irão escrever a mensagem específica no Streamlit.
    st.info(st.session_state.get('explicacao'))
    
    if st.button("Reiniciar Verificação de Notas"):
        for fact_id, fact in ManualEngine.facts.items():
            if isinstance(fact, Nota1) or isinstance(fact, Nota2):
                ManualEngine.retract(fact_id)
        st.session_state['nota1_informada'] = False
        st.session_state['nota2_informada'] = False
        st.session_state['carregarPagina'] = 'perguntarNotas' # Volta para o início das perguntas
