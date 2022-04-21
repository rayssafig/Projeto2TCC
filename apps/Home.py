import streamlit as st


def app():

    titl, imga = st.columns((4, 1))
    imga.image('E_SDG_logo_UN_emblem_square_trans_WEB.png')
    titl.title('Mapeando os Indicadores dos Objetivos de Desenvolvimento Sustentável da ONU')
    st.write('Seja bem-vindo a essa aplicação _open-source_, reprodutível, para visualizar dados e mapas relacionados aos Objetivos de Desenvolvimento Sustentável (ODS) e seus indicadores.')

    st.markdown("""
        A aplicação é resultado de um Trabalho de Conclusão de Curso de Engenharia Cartográfica e de Agrimensura da Universidade Federal do Paraná, e tem o objetivo de apresentar diferentes utilizações da cartografia para representar os ODS e seus indicadores, através de mapas interativos, gráficos e tabelas oriundos de fontes livres
        e bibliotecas *python* como [folium](https://python-visualization.github.io/folium/modules.html), [geopandas](https://geopandas.org/), [leafmap](https://leafmap.org), [matplotlib](https://matplotlib.org/), [requests](https://docs.python-requests.org/), e [pandas](https://pandas.pydata.org/).""")

    st.info("🚨 **Selecione no menu à esquerda para navegar entre as diferentes aplicações** 🚨 ")

    st.subheader("Introdução")
    st.markdown("""Os Objetivos de Desenvolvimento Sustentável são um apelo global à ação para acabar com a pobreza, proteger o meio ambiente e o clima e garantir que as pessoas, em todos os lugares, possam desfrutar de paz e de prosperidade (ONU Brasil, 2022).
                A cartografia tem papel fundamental nesta tarefa ao promover discussões acerca de como atingir os objetivos com o uso de dados e representações visuais que auxiliam em análises e na tomada de decisões.""")
    st.write('Os 17 Objetivos de Desenvolvimento Sustentável foram definidos como parte da Agenda 2030, com foco em três grandes áreas do desenvolvimento sustentável: social, econômica e ambiental, apresentados como:')

    imga, titl = st.columns((0.3, 5))
    titl.write('**Erradicação da Pobreza**')
    imga.image('E-WEB-Goal-01.png')

    imga, titl = st.columns((0.3, 5))
    titl.write('**Fome zero e agricultura sustentável**')
    imga.image('E-WEB-Goal-02.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Saúde e Bem-Estar**')
    imga.image('E-WEB-Goal-03.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Educação de Qualidade**')
    imga.image('E-WEB-Goal-04.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Igualdade de gênero**')
    imga.image('E-WEB-Goal-05.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Água potável e saneamento**')
    imga.image('E-WEB-Goal-06.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Energia limpa e acessível**')
    imga.image('E-WEB-Goal-07.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Trabalho decente e crescimento econômico**')
    imga.image('E-WEB-Goal-08.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Indústria, inovação e infraestrutura**')
    imga.image('E-WEB-Goal-09.png')

    imga, titl = st.columns((0.3, 5))
    titl.write('**Redução das desigualdades**')
    imga.image('E-WEB-Goal-10.png')

    imga, titl = st.columns((0.3, 5))
    titl.write('**Cidades e comunidades sustentáveis**')
    imga.image('E-WEB-Goal-11.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Consumo e produção responsáveis**')
    imga.image('E-WEB-Goal-12.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Ação contra a mudança global do clima**')
    imga.image('E-WEB-Goal-13.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Vida na água**')
    imga.image('E-WEB-Goal-14.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Vida terrestre**')
    imga.image('E-WEB-Goal-15.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Paz, justiça e instituições eficazes**')
    imga.image('E-WEB-Goal-16.png')
    
    imga, titl = st.columns((0.3, 5))
    titl.write('**Parceria e meios de implementação**')
    imga.image('E-WEB-Goal-17.png')

    st.write('O objetivo principal dessa aplicação é apresentar dados espaciais e análises que representem os ODS e seus indicadores e possam servir de modelo e inspiração para criação de ***dashboards*** e representações espaciais que auxiliem no monitoramento do desenvolvimento sustentável e tomada de decisões no alcance das metas propostas pelas ONU.')
             
    st.write('Com foco em promover análises geoespaciais, dados abertos, espaciais e não espaciais foram utilizados para permitir ao usuário visualizar diferentes recortes geográficos,'
             ' a nível municipal, estadual, nacional e global.')

    st.info('🧭 Aproveite a experiência e navegue pelas diferentes páginas para visualizar os ODS. 🔍')

    st.markdown("## Obrigada por utilizar essa aplicação!")
    st.info('Essa aplicação usa a biblioteca **Streamlit**. O código fonte encontra-se disponível no [GitHub](https://github.com/rayssafig/Projeto2TCC) 👾')
    btn = st.button("Mantido por Rayssa Figueiredo")
    if btn:
        st.balloons()

