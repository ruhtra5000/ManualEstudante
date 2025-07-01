from experta import *
from engine_parts.facts import *
import streamlit as st

#Motor de inferencia com definição das regras
class Manual(KnowledgeEngine):
    #Função para debug
    def imprimirFatos(self):
        print("\nFatos atuais:")
        print(self.facts)

    #Regras
    #Matricula
    @Rule(MatriculaEntrada(txt = "semestre"))
    def matrSemestral(self):
        st.write("A matrícula é da responsabilidade do(a) aluno(a) e deve ser " + 
                "renovada semestralmente, obedecendo às datas divulgadas no " + 
                "Calendário Acadêmico disponível no site da UFAPE, para o " + 
                "prosseguimento de estudos, observando-se a sequência estabelecida no " + 
                "currículo, os pré-requisitos e a compatibilidade de horários. Toda a " + 
                "orientação necessária à matrícula pode ser obtida junto à Coordenação " + 
                "do Curso e à Comissão de Orientação e Acompanhamento Acadêmico " + 
                "(COAA) do seu respectivo Curso.")

    @Rule(MatriculaEntrada(txt = "reajuste"))
    def matrReajuste(self):
        st.write("Para aquele aluno que efetuou a matrícula regular, mas deseja " +
                "permutar ou excluir disciplina(s). A efetivação do reajuste da matrícula " +
                "só ocorre se ainda houver vaga nas disciplinas que ele permutou, " +
                "ficando em fila de espera classificada pelo ranking.")
    

    #Disciplina
    @Rule(DisciplinaEntrada(txt = "cancelamento"))
    def cancelamentoDisciplina(self):
        st.write("Em datas pré-estabelecidas, no Calendário Acadêmico, o(a) aluno(a) " +
            "poderá requerer cancelamento de uma ou mais disciplinas. No caso de " +
            "alunos diurnos, só poderão cancelar duas disciplinas do bloco principal.")

        #"Explicabilidade"
        st.info("Definido pela p.25 do Manual do Estudante 2023")
    
    @Rule(DisciplinaEntrada(txt = "dispensa"))
    def dispensaDisciplina(self):
        '''st.header("Disciplina")
        st.write("Disciplinas são legais")'''
        #Falta adicionar a explicabilidade 


    #Cancelamento de vínculo
    @Rule(CancelamentoEntrada(txt = "lorem ipsum"))
    def cancelPadrao(self):
        '''st.header("Cancelamento de vínculo")
        st.write("O cancelamento de registro acadêmico é o desligamento efetivo da UFAPE.")'''
        #Falta adicionar a explicabilidade 