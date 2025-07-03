import streamlit as st
from engine_parts.engine_instance import ManualEngine
from engine_parts.facts import *
from interface.widgets import campoTexto, campoOpcao, campoNumero

def apoioEstudantil():
    st.header("Apoio Estudantil")
    st.write(
        "Os programas de apoio aos estudantes de graduação da UFAPE são iniciativas que visam oferecer suporte " +
        "financeiro, psicológico, pedagógico e social para garantir a permanência e o bom desempenho dos estudantes. " +
        "Esses programas incluem auxílios como moradia, alimentação, transporte, material didático, além de ações " +
        "de acompanhamento e orientação estudantil. Para mais informações, consulte o site oficial da UFAPE ou o setor de assistência estudantil.")

    entrada = campoTexto(
        chave="apoio_estudantil",
        texto_label="Deseja saber algo mais sobre apoio estudantil?",
        texto_placeholder="Ex.: Bolsas, Auxílios, Programas de apoio",
    )
    
    if entrada:
        ManualEngine.declare(ApoioEstudantilEntrada(txt=entrada))
        ManualEngine.imprimirFatos()
        ManualEngine.run()

    match(st.session_state.get('carregarPagina')):
        case 'apoioEstudantilMonitoria':
            apoioEstudantilMonitoria()
        case 'apoioEstudantilPet':
            apoioEstudantilPet()
        case 'apoioEstudantilBia':
            apoioEstudantilBia()
        case 'apoioEstudantilPavi':
            apoioEstudantilPavi()
        case 'apoioEstudantilPibid':
            apoioEstudantilPibid()
        case 'apoioEstudantilPibic':
            apoioEstudantilPibic()
        case 'apoioEstudantilPrp':
            apoioEstudantilPrp()
        case 'apoioEstudantilExtensao':
            apoioEstudantilExtensao()
        case 'apoioEstudantilMobilidade':
            apoioEstudantilMobilidade()
        case 'apoioEstudantilPai':
            apoioEstudantilPai()
        case 'apoioEstudantilPad':
            apoioEstudantilPad()
        case 'apoioEstudantilResidencia':
            apoioEstudantilResidencia()
        case 'apoioEstudantilVoltaAoLar':
            apoioEstudantilVoltaAoLar()
        case 'apoioEstudantilPag':
            apoioEstudantilPag()
        case 'apoioEstudantilCultura':
            apoioEstudantilCultura()
        case 'apoioEstudantilRural':
            apoioEstudantilRural()
        case 'apoioEstudantilRemt':
            apoioEstudantilRemt()
        case 'apoioEstudantilAcessibilidade':
            apoioEstudantilAcessibilidade()
        case 'apoioEstudantilFinalBolsas':
            apoioEstudantilFinalBolsas()
        case 'apoioEstudantilFinalAuxilios':
            apoioEstudantilFinalAuxilios()
        case 'apoioEstudantilFinal':
            apoioEstudantilFinal()

        #Perguntas sobre bolsas

        case 'perguntaMonitoria':
            perguntaMonitoria()
        case 'perguntaPet':
            perguntaPet()
        case 'perguntaBia':
            perguntaBia()
        case 'perguntaPibid':
            perguntaPibid()
        case 'perguntaPibic':
            perguntaPibic()
        case 'perguntaPrp':
            perguntaPrp()
        case 'perguntaExtensao':
            perguntaExtensao()

        #Perguntas sobre auxílios
        case 'perguntaMobilidade':
            perguntaMobilidade()
        case 'perguntaPai':
            perguntaPai()
        case 'perguntaPad':
            perguntaPad()
        case 'perguntaResidencia':
            perguntaResidencia()
        case 'perguntaVoltaAoLar':
            perguntaVoltaAoLar()
        case 'perguntaPag':
            perguntaPag()
        case 'perguntaRural':
            perguntaRural()

        #Perguntas sobre apoio
        case 'perguntaPavi':
            perguntaPavi()
        case 'perguntaCultura':
            perguntaCultura()
        case 'perguntaRemt':
            perguntaRemt()
        case 'perguntaAcessibilidade':
            perguntaAcessibilidade()

#Interface para o programa de monitoria
def apoioEstudantilMonitoria():
    st.write("Programa de monitoria:" + 
            "\n\nObjetiva incentivar os(as) alunos(as) que " +
            "demonstrarem interesse e aptidão pela carreira acadêmica, " +
            "assegurando a cooperação do corpo discente ao corpo docente nas " +
            "atividades do ensino. Oferece duas categorias: Monitor Bolsista e Monitor Voluntário. ")

    st.info(st.session_state.get('explicacao'))

#Interface para o programa PET
def apoioEstudantilPet():
    st.write("Programa de Educação Tutorial (PET): " +
            "\n\nÉ destinado a grupos de alunos que demonstrem potencial, interesse e habilidade destacados em vários " +
            "cursos da Universidade. É integrado por grupos tutoriais de " +
            "aprendizagem e tem por objetivo promover a formação ampla e de " +
            "qualidade dos (as) alunos (as) de graduação envolvidos direta ou " +
            "indiretamente com o programa, estimulando a fixação de valores que " +
            "reforcem a cidadania e a consciência social dos participantes e a " +
            "melhoria dos cursos. Na UFAPE existem três grupos: Conexões dos " +
            "Saberes, Biotecnologia e Criativação.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para o programa BIA
def apoioEstudantilBia():
    st.write("Bolsa de Incentivo Acadêmica (BIA): " +
            "\n\nO objetivo do programa é favorecer a adaptação à vida acadêmica " +
            "universitária de alunos no 1º ano do curso da UFAPE (preferencialmente " +
            "Licenciatura) que tenham sido egressos das escolas públicas da Rede " +
            "Estadual de Pernambuco, por meio de ajuda financeira, desenvolvendo, " +
            "sob a supervisão de docente do curso, atividades acadêmicas que " +
            "contribuam para o fortalecimento do ensino público e incentivem " +
            "outros (as) alunos (as) da rede pública a dar continuidade aos estudos " +
            "após a conclusão do Ensino Médio.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para o programa PAVI
def apoioEstudantilPavi():
    st.write("Programa de Atividade de Vivência Interdisciplinar (PAVI): " +
            "\n\nTem o objetivo de oportunizar e promover, dentro do processo " +
            "ensino-aprendizagem, o treinamento das aptidões e habilidades técnicas " +
            "dos discentes da UFAPE, sob orientação, por meio da interconexão entre " +
            "os conteúdos teórico-práticos dos diversos componentes curriculares, " +
            "sobretudo práticos, envolvendo as diversas áreas do conhecimento e à " +
            "luz dos Projetos Pedagógicos dos Cursos (PPC's). Tem caráter voluntário, " +
            "não possui bolsas e as vagas são disponibilizadas por meio de Edital " +
            "divulgado no site da Universidade.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para o programa PIBID
def apoioEstudantilPibid():
    st.write("Programa de Iniciação à Docência (PIBID): " +
            "\n\nTem como objetivo fomentar a iniciação à docência de estudantes dos " +
            "cursos de licenciatura da UFAPE, contribuir para a formação continuada " +
            "dos professores da educação básica em Pernambuco e, em consequência, " +
            "melhorar o desempenho dos estudantes das redes municipais e " +
            "estadual de ensino. Atualmente o programa é gerenciado pela " +
            "Coordenação Geral de Cursos de Graduação.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para o programa PIBIC
def apoioEstudantilPibic():
    st.write("Programa de Iniciação Cientifica (PIBIC/CNPq): " +
            "\n\nO objetivo do programa é incentivar o(a) estudante a se envolver com a " +
            "pesquisa científica na Universidade, dando-lhe maior motivação na " +
            "realização do seu curso e melhores condições de aprendizagem. O(a) " +
            "aluno(a) deve entrar em contato com um professor orientador, elaborando " +
            "um projeto para concorrer à bolsa. Fique atento ao Edital anual do PIBIC. " +
            "Anualmente os trabalhos são apresentados no Congresso de Iniciação " +
            "Científica (CIC).")
    
    st.info(st.session_state.get('explicacao'))

#Interface para o programa PRP
def apoioEstudantilPrp():
    st.write("Programa de Residência Pedagógica (PRP): " +
            "\n\nTem como objetivos: aperfeiçoar a formação dos discentes de cursos de " +
            "licenciatura, por meio do desenvolvimento de projetos que fortaleçam o " +
            "campo da prática e conduzam o licenciado a exercitar de forma ativa a " +
            "relação entre teoria e prática profissional docente, utilizando coleta de " +
            "dados e diagnóstico sobre o ensino e aprendizagem escolar, entre outras " +
            "didáticas e metodologias; induzir a reformulação do estágio supervisionado " +
            "nos cursos de licenciatura, tendo como base a experiência da residência " +
            "pedagógica; fortalecer, ampliar e consolidar a relação entre a IES e a escola, " +
            "promovendo sinergia entre a entidade que forma e a que recebe o egresso da " +
            "licenciatura e estimulando o protagonismo da rede de ensino na formação dos " +
            "professores; e promover a adequação dos currículos e propostas pedagógicas " +
            "dos cursos de formação inicial de professores de educação básica às " +
            "orientações da Base Comum Curricular (BNCC).")
    
    st.info(st.session_state.get('explicacao'))

#Interface para o programa de extensão
def apoioEstudantilExtensao():
    st.write("Programas de Extensão: " +
            "\n\nTêm por objetivo atender aos(às) alunos(as) que tenham interesse em se " +
            "integrar nas atividades de extensão, em projetos dirigidos para a ação " +
            "comunitária. Alguns programas são direcionados a uma ação social relevante, " +
            "como é o caso do Programa de Alfabetização. Anualmente os trabalhos dos " +
            "bolsistas são apresentados no Congresso de Extensão (CONEX).")
    
    st.info(st.session_state.get('explicacao'))

#Interface para o programa de mobilidade acadêmica
def apoioEstudantilMobilidade():
    st.write("Programa de Mobilidade Acadêmica: " +
            "\n\nOs estudantes dos cursos de graduação da UFAPE podem obter vínculo " +
            "temporário em qualquer das instituições federais de ensino superior " +
            "(Universidades e Institutos Federais, vinculados à Andifes), por até dois " +
            "semestres letivos, para cumprirem disciplinas e/ou estágios, devendo, para " +
            "tanto, programar um plano de atividades acadêmicas a serem cumpridas na " +
            "outra IES, preferencialmente sob a orientação do Coordenador de seu Curso " +
            "e requerer a mobilidade acadêmica. Para maiores informações os estudantes " +
            "interessados deverão procurar a Coordenação Geral de Cursos.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para o programa PAI
def apoioEstudantilPai():
    st.write("Programa de Apoio ao Ingressante (PAI): " +
            "\n\nTem por finalidade apoiar os alunos ingressantes de recorte social, " +
            "com bolsa temporária de 3 meses até que o mesmo conheça a Instituição e " +
            "possa concorrer a vagas em programas de permanência. ")
    
    st.info(st.session_state.get('explicacao'))

#Interface para o programa PAD
def apoioEstudantilPad():
    st.write("Programa de Apoio ao Discente (PAD): " +
            "\n\nSe refere ao antigo Programa de Bolsas de Permanência, o qual foi " +
            "modificado na Resolução Nº 237/2014 do CEPE. Este programa baseia-se em " +
            "três modalidades de benefícios: Bolsa de Apoio Acadêmico e Auxílios " +
            "Transporte e Alimentação. ")
    
    st.info(st.session_state.get('explicacao'))

#Interface para o programa de residência estudantil
def apoioEstudantilResidencia():
    st.write("Programa de Residência Estudantil: " +
            "\n\nTem por objetivo priorizar a permanência de discentes com recorte social " +
            "originários de outros Estados ou que não residam no município de Garanhuns. " +
            "Os(as) discentes selecionados(as) para residência recebem Auxílio Manutenção " +
            "e quando não há vaga, na disponibilidade de recurso financeiro, o Auxílio " +
            "Moradia pode ser implementado.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para o programa PAG
def apoioEstudantilPag():
    st.write("Programa de Apoio à Gestante (PAG): " +
            "\n\nOs estudantes dos cursos de graduação da UFAPE podem obter vínculo " +
            "temporário em qualquer das instituições federais de ensino superior " +
            "(Universidades e Institutos Federais, vinculados à Andifes), por até dois " +
            "semestres letivos, para cumprirem disciplinas e/ou estágios, devendo, para " +
            "tanto, programar um plano de atividades acadêmicas a serem cumpridas na " +
            "outra IES, preferencialmente sob a orientação do Coordenador de seu Curso " +
            "e requerer a mobilidade acadêmica. Para maiores informações os estudantes " +
            "interessados deverão procurar a Coordenação Geral de Cursos.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para o programa de volta ao lar
def apoioEstudantilVoltaAoLar():
    st.write("Programa de Volta ao Lar: " +
            "\n\nTem por finalidade custear, uma vez em cada semestre, ajuda de custo " +
            "para os discentes residentes visitarem seus familiares durante o recesso escolar.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para o programa de incentivo a cultura
def apoioEstudantilCultura():
    st.write("Programa de Incentivo à Cultura: " +
            "\n\nTem por finalidade incentivar discentes matriculados em cursos de " +
            "graduação presenciais à prática musical com participações em eventos " +
            "estudantis, regionais, estaduais e nacionais através do Coral Universitário " +
            "com a concessão de Bolsa Coral Universitário.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para o programa de hospeda rural
def apoioEstudantilRural():
    st.write("Programa Hospeda Rural: " +
            "\n\nTem como objetivo liberar o Auxílio Recepção/Hospedagem para alunos de " +
            "graduação da UFAPE quando recebem alunos estrangeiros em sua residência, " +
            "através da Cooperação Internacional.")
                
    st.info(st.session_state.get('explicacao'))

#Interface para o programa REMT
def apoioEstudantilRemt():
    st.write("Regime Especial de Movimentação Temporária (REMT): " +
            "\n\nDisciplina a movimentação de estudantes, através da qual os mesmos podem " +
            "cursar blocos (Regime seriado) ou disciplinas isoladas (Créditos) temporariamente " +
            "em uma Unidade Acadêmica da UFRPE diferente da sua Unidade de origem.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para secretaria de acessibilidade
def apoioEstudantilAcessibilidade():
    st.write("Secretaria de Acessibilidade: " +
            "\n\nA Secretaria integra uma rede de Núcleos de Acessibilidade, fomentada nas " +
            "Instituições Federais de Ensino Superior (IFES) por meio do “Programa Incluir” " +
            "e tem o papel de atuar na identificação de demandas e na proposição e " +
            "dinamização de ações institucionais de acessibilidade. Além das diversas " +
            "atividades no âmbito administrativo, no campo do desenvolvimento de ações " +
            "de acessibilidade em nossa IFES, a Acessibilidade também oferece serviços de " +
            "atendimento ao seu público-alvo." + 
            "\n\nObjetivo da Secretaria de Acessibilidade: " +
            "\n\nPropor, desenvolver e promover ações de acessibilidade que visem a " +
            "eliminação de barreiras İsicas/arquitetônicas, pedagógicas, atitudinais e " +
            "comunicacionais na UFAPE. " +
            "\n\nServiços " +
            "\n\n1- Apoio Pedagógico ao Discente com necessidade de Acessibilidade; " +
            "\n\n2- Tradução e Interpretação em LIBRAS/Português de textos, aulas, " +
            "eventos e atividades promovidas pela UFAPE.")
    
    st.info(st.session_state.get('explicacao'))

#Interface para final das bolsas
def apoioEstudantilFinalBolsas():
    st.write("Não possuimos mais opções de bolsas disponíveis")

#Interface para final dos auxilios
def apoioEstudantilFinalAuxilios():
    st.write("Não possuimos mais opções de auxilios disponíveis")

#Interface para final do apoio
def apoioEstudantilFinal():
    st.write("Não possuimos mais opções de apoio disponíveis")

#Pergunta sobre monitória
def perguntaMonitoria():
    resposta = campoOpcao (
        'Monitoria',
        'Você tem interesse no programa de monitoria?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(InteresseMonitoria(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(InteresseMonitoria(tipo = True))

#Pergunta sobre PET
def perguntaPet():
    resposta = campoOpcao (
        'Pet',
        'Você tem interesse no programa de educação tutorial?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(InteressePet(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(InteressePet(tipo = True))

#Pergunta sobre BIA
def perguntaBia():
    resposta = campoOpcao (
        'Bia',
        'Você tem interesse no programa de incentivo acadêmico?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(InteresseBia(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(InteresseBia(tipo = True))

#Pergunta sobre PIBID
def perguntaPibid():
    resposta = campoOpcao (
        'Pibid',
        'Você tem interesse no programa de iniciação a docência?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(InteressePibid(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(InteressePibid(tipo = True))

#Pergunta sobre PIBIC
def perguntaPibic():
    resposta = campoOpcao (
        'Pibic',
        'Você tem interesse no programa de iniciação ciêntifica?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(InteressePibic(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(InteressePibic(tipo = True))

#Pergunta sobre PRP
def perguntaPrp():
    resposta = campoOpcao (
        'Prp',
        'Você tem interesse no programa de residência pedagógica?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(InteressePrp(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(InteressePrp(tipo = True))

#Pergunta sobre Extensão
def perguntaExtensao():
    resposta = campoOpcao (
        'Extensao',
        'Você tem interesse no programa de extensão?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(InteresseExtensao(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(InteresseExtensao(tipo = True))

#Pergunta sobre Mobilidade
def perguntaMobilidade():
    resposta = campoOpcao (
        'Mobilidade',
        'Você tem interesse no programa de mobilidade acadêmica?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(InteresseMobilidade(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(InteresseMobilidade(tipo = True))

#Pergunta sobre Pai
def perguntaPai():
    resposta = campoOpcao (
        'Pai',
        'Você tem interesse no programa de apoio ao ingressante?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(InteressePai(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(InteressePai(tipo = True))

#Pergunta sobre PAD
def perguntaPad():
    resposta = campoOpcao (
        'Pad',
        'Você tem interesse no programa de apoio ao discente?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(InteressePad(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(InteressePad(tipo = True))

#Pergunta sobre Residência
def perguntaResidencia():
    resposta = campoOpcao (
        'Residencia',
        'Você tem interesse no programa de residência estudantil?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(InteresseResidencia(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(InteresseResidencia(tipo = True))

#Pergunta sobre Volta ao Lar
def perguntaVoltaAoLar():
    resposta = campoOpcao (
        'VoltaAoLar',
        'Você tem interesse no programa de volta ao lar?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(InteresseVoltaAoLar(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(InteresseVoltaAoLar(tipo = True))

#Pergunta sobre PAG
def perguntaPag():
    resposta = campoOpcao (
        'Pag',
        'Você tem interesse no programa de apoio à gestante?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(InteressePag(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(InteressePag(tipo = True))

#Pergunta sobre Rural
def perguntaRural():
    resposta = campoOpcao (
        'Rural',
        'Você tem interesse no programa de hospedagem rural?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(InteresseRural(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(InteresseRural(tipo = True))

#Pergunta sobre PAVI
def perguntaPavi():
    resposta = campoOpcao (
        'Pavi',
        'Você tem interesse no programa de atividade de vivência interdisciplinar?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(InteressePavi(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(InteressePavi(tipo = True))

#Pergunta sobre Cultura
def perguntaCultura():
    resposta = campoOpcao (
        'Cultura',
        'Você tem interesse no programa de incentivo à cultura?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(InteresseCultura(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(InteresseCultura(tipo = True))

#Pergunta sobre REMT
def perguntaRemt():
    resposta = campoOpcao (
        'Remt',
        'Você tem interesse no Regime Especial de Movimentação Temporária (REMT)?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(InteresseRemt(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(InteresseRemt(tipo = True))

#Pergunta sobre Acessibilidade
def perguntaAcessibilidade():
    resposta = campoOpcao (
        'Acessibilidade',
        'Você tem interesse nos serviços de acessibilidade da UFAPE?',
        ['Sim', 'Não']
    )

    if not resposta is None and resposta == 'não':
        ManualEngine.declare(InteresseAcessibilidade(tipo = False))

    elif not resposta is None and resposta == 'sim':
        ManualEngine.declare(InteresseAcessibilidade(tipo = True))


