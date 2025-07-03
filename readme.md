
# 📘 Manual do Estudante

Este projeto é um Manual do Estudante interativo, desenvolvido como parte da disciplina de Inteligência Artificial na Universidade Federal do Agreste de Pernambuco (UFAPE).

Seu objetivo é auxiliar discentes da UFAPE a esclarecer dúvidas sobre normas acadêmicas e procedimentos institucionais por meio de um sistema especialista baseado em regras. O motor de inferência processa perguntas e fornece respostas e direcionamentos automáticos, simulando o comportamento de um atendente virtual.

👨‍💻 Discentes
- Arthur de Sá Tenório
- Guilherme Paes Cavalcanti
- Victor Cauã Tavares Inácio

**Disciplina**: Inteligência Artificial  
**Professor**: Luis Filipe Alves Pereira  
**Período**: 5º Período (2025.1)  
**Instituição**: Universidade Federal do Agreste de Pernambuco (UFAPE)

---


### 🧠 Tecnologias utilizadas

- Python — linguagem de programação principal  
- Experta — motor de inferência baseado em regras  
- Streamlit — framework para criação de interfaces web interativas  

---

### 🚀 Como executar o projeto

Siga os passos abaixo para rodar a aplicação localmente:

1. Instale o Python  
   Baixe e instale o Python pela página oficial: https://www.python.org/downloads/  
   Recomenda-se a versão 3.9 ou inferior para evitar ajustes manuais no código-fonte de dependências.

2. Instale as dependências  
   `pip install experta streamlit`

   ⚠️ Atenção: Se estiver utilizando Python 3.10 ou superior, será necessário ajustar a biblioteca `experta`:
   - Acesse o arquivo `__init__.py` da biblioteca `experta`
   - Substitua a linha:
     from collections
     Por:
     import collections.abc as collections

3. Execute o projeto  
   `python -m streamlit run main.py`

---
