import streamlit as st
from engine_parts.engine_instance import ManualEngine
from engine_parts.facts import *
from interface.widgets import campoTexto

def colacaoGrau():
    st.header("Colação de Grau")
    st.write(
        "A colação de grau ocorre após o(a) aluno(a) integralizar todos os componentes do curso, incluindo o ENADE e as atividades complementares. " +
        "Ela é realizada em sessão solene e pública com todos os cursos de graduação, presidida pelo(a) Reitor(a) da UFAPE.")

    entrada = campoTexto(
        chave="colacao_grau",
        texto_label="Deseja saber algo mais sobre colação de grau?",
        texto_placeholder="Ex.: Colação em separado, Aluno laureado"
    )

    if entrada:
        ManualEngine.declare(ColacaoGrauEntrada(txt=entrada))
        ManualEngine.imprimirFatos()
        ManualEngine.run()

    match(st.session_state.get('carregarPagina')):
        case 'colacaoEmSeparado':
            colacaoEmSeparado()
        case 'colacaoAlunoLaureado':
            colacaoAlunoLaureado()

#Interface para colação em separado
def colacaoEmSeparado():
    st.write("O(a) aluno(a) que precisar antecipar sua colação de grau poderá requerê-la em separado. " +
            "Para tanto, o Coordenador do Curso deverá formalizar o requerimento de Colação de Grau, " +
            "justificando (e documentando) o motivo. Este aluno irá receber o grau em sessão solene, " +
            "em separado, presidida pelo Reitor ou seu representante, com a presença de pelo menos três " +
            "professores do Curso. O(a) aluno(a) deverá estar presente na solenidade, na sua ausência, " +
            "poderá ser substituído nesse ato por representante com procuração.")

    st.info(st.session_state.get('explicacao'))

#Interface para colação de grau de aluno laureado
def colacaoAlunoLaureado():
    st.write("O(a) aluno(a) que tiver o melhor coeficiente de rendimento escolar (média geral mais alta) " +
            "e que não apresentar reprovações em seu Histórico Escolar, será conferido uma láurea e " +
            "expedido um Certificado correspondente, entregue pelo Reitor da Universidade, durante a " +
            "Cerimônia de Colação de Grau.")
    
    st.info(st.session_state.get('explicacao'))