import streamlit as st
from engine_parts.engine_instance import ManualEngine
from interface.widgets import campoTexto, campoOpcao

def direitosDeveresInicial():
    st.header("Direitos e Deveres do Estudante")
    st.write("Aqui você encontra informações sobre os direitos e deveres dos estudantes da UFAPE, incluindo questões de ética acadêmica, conduta, e direitos estudantis.")

    st.subheader("Sobre Direitos...")
    st.markdown("- Receber um ensino de qualidade.")
    st.markdown("- Participar de todas as atividades da vida universitária.")
    st.markdown("- Ter acesso a todas as informações sobre a Universidade e às rotinas da vida acadêmica.")
    st.markdown("- Organizar-se em Diretórios Acadêmicos e no Diretório Central dos Estudantes (DCE).")
    st.markdown("- Ser representado em todos os órgãos colegiados da administração da UFAPE.")
    st.markdown("---")
    
    st.subheader("Sobre Deveres...")
    st.markdown("- Valorizar a vaga pública que conquistou.")
    st.markdown("- Cuidar do patrimônio da Universidade.")
    st.markdown("- Respeitar todos os membros da comunidade universitária.")
    st.markdown("- Obedecer à Legislação da Universidade.")
    st.markdown("- Conferir e solicitar correção do comprovante de matrícula e do seu histórico escolar.")