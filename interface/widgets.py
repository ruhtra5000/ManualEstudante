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

def campoNumero(
    chave: str,
    texto_label: str,
    minimo: float,
    maximo: float
): 
    """Renderiza um campo de número com formulário e retorna o numero inserido."""
    
    with st.form(key=f"{chave}_form"):
        entrada = st.number_input(
            label=texto_label,
            key=f"{chave}_number",
            min_value=minimo,
            max_value=maximo
        )
        submitted = st.form_submit_button("Enviar")

    if submitted and entrada is not None:
        return entrada
    
    return None

def campoOpcao(
    chave: str,
    texto_label: str,
    opcoes: list[str]
):
    """Renderiza uma pergunta com opções restritas e retorna a opção selecionada."""
    
    with st.form(key=f"{chave}_form"):
        escolha = st.radio(
            texto_label,
            opcoes,
            key=f"{chave}_radio"
        )
        submitted = st.form_submit_button("Enviar")

    if submitted:
        return escolha.lower().strip()
    
    return None