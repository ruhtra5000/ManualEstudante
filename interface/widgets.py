import streamlit as st

#Arquivo que contém elementos de interface personalizados, 
#que podem ser reutilizados

def campoTexto(
    chave: str,
    texto_label: str,
    texto_placeholder: str
): 
    """Renderiza um campo de texto com formulário e retorna o texto submetido."""
    
    with st.form(key=f"{chave}_form"):
        entrada = st.text_input(
            texto_label,
            placeholder=texto_placeholder,
            key=f"{chave}_input"
        )
        submitted = st.form_submit_button("Enviar")

    if submitted and entrada.strip():
        return entrada.lower().strip()
    
    return None