# Manual do Estudante

projeto de IA bla bla bla...

## Como rodar o projeto

1. Instalar o [Python](https://www.python.org/downloads/)
2. Usar o comando `pip install experta`
3. Usar o comando `pip install streamlit`
4. Caso seu Python esteja na versão 3.10+ é preciso: 
    - Acessar o arquivo __init__.py do Experta; e
    - Mudar a linha 1 de: `from collections` 
    - Para `import collections.abc as collections`
5. Por fim, basta usar o comando `python -m streamlit run main.py` para rodar o projeto