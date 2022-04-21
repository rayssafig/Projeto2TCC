import streamlit as st
from streamlit_folium import folium_static
import folium
import geopandas as gpd
import plotly.express as px
import functools

chart = functools.partial(st.plotly_chart, use_container_width=True)
COMMON_ARGS = {
    "color": "parentName",
    "color_discrete_sequence": px.colors.sequential.Cividis,
    "hover_data": [
        'latest_value',
    ], }


def app():
    global data
    titl, imga = st.columns((4, 0.8))
    imga.image('E-WEB-Goal-02.png')
    titl.title('ODS 2: Fome zero e agricultura sustentável')
    st.subheader('Objetivo: Erradicar a fome, alcançar a segurança alimentar, melhorar a nutrição e promover a agricultura sustentável')
    st.write('*O rápido crescimento econômico e o aumento da produção agrícola nas últimas duas décadas fizeram com que o número de pessoas em má-nutrição caísse quase pela metade. Muitos países em desenvolvimento que sofriam com a fome agora podem suprir as necessidades dos mais vulneráveis. Ásia central, Sudeste Asiático, América Latina e o Caribe são regiões que fizeram grandes progressos para erradicar  a fome extrema.* (PNUD, 2022)')
    st.write('A meta de acabar com todas as formas de fome e a má-nutrição até 2030, envolve compreender o atual cenário da fome no mundo. Cada país enfrenta uma realidade diferente e suas metas devem ser planejadas de acordo com sua situação.'
             ' A seguir, resultados de análises detalhadas sobre a situação da fome no globo.')

    with st.expander('Saber mais sobre os Indicadores do Objetivo 2'):
        st.write("""**2.1** Até 2030, acabar com a fome e garantir o acesso de todas as pessoas, em particular os pobres e pessoas em situações vulneráveis, incluindo crianças, a alimentos seguros, nutritivos e suficientes durante todo o ano 
        \n **2.2** Até 2030, acabar com todas as formas de desnutrição, incluindo atingir, até 2025, as metas acordadas internacionalmente sobre nanismo e caquexia em crianças menores de cinco anos de idade, e atender às necessidades nutricionais dos adolescentes, mulheres grávidas e lactantes e pessoas idosas
        \n **2.3** Até 2030, dobrar a produtividade agrícola e a renda dos pequenos produtores de alimentos, particularmente das mulheres, povos indígenas, agricultores familiares, pastores e pescadores, inclusive por meio de acesso seguro e igual à terra, outros recursos produtivos e insumos, conhecimento, serviços financeiros, mercados e oportunidades de agregação de valor e de emprego não agrícola
        \n **2.4** Até 2030, garantir sistemas sustentáveis de produção de alimentos e implementar práticas agrícolas resilientes, que aumentem a produtividade e a produção, que ajudem a manter os ecossistemas, que fortaleçam a capacidade de adaptação às mudanças climáticas, às condições meteorológicas extremas, secas, inundações e outros desastres, e que melhorem progressivamente a qualidade da terra e do solo
        \n **2.5** Até 2020, manter a diversidade genética de sementes, plantas cultivadas, animais de criação e domesticados e suas respectivas espécies selvagens, inclusive por meio de bancos de sementes e plantas diversificados e bem geridos em nível nacional, regional e internacional, e garantir o acesso e a repartição justa e equitativa dos benefícios decorrentes da utilização dos recursos genéticos e conhecimentos tradicionais associados, como acordado internacionalmente
        \n **2.a** Aumentar o investimento, inclusive via o reforço da cooperação internacional, em infraestrutura rural, pesquisa e extensão de serviços agrícolas, desenvolvimento de tecnologia, e os bancos de genes de plantas e animais, para aumentar a capacidade de produção agrícola nos países em desenvolvimento, em particular nos países menos desenvolvidos
        \n **2.b** Corrigir e prevenir as restrições ao comércio e distorções nos mercados agrícolas mundiais, incluindo a eliminação paralela de todas as formas de subsídios à exportação e todas as medidas de exportação com efeito equivalente, de acordo com o mandato da Rodada de Desenvolvimento de Doha
        \n **2.c** Adotar medidas para garantir o funcionamento adequado dos mercados de commodities de alimentos e seus derivados, e facilitar o acesso oportuno à informação de mercado, inclusive sobre as reservas de alimentos, a fim de ajudar a limitar a volatilidade extrema dos preços dos alimentos""")
    
    hunger = gpd.read_file(
        'https://services7.arcgis.com/gp50Ao2knMlOM89z/arcgis/rest/services/SN_ITK_DEFC_2_1_1_2020Q2G03/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson')

    st.subheader('Prevalência de subnutrição por país')
    m = folium.Map(location=[26.972058, 28.642816], tiles='Stamen Water Color', zoom_start=1.5, control_scale=True)
    folium.GeoJson(
        hunger,
        name='Percentual',
        popup="última proporção conhecida: ",
        tooltip=folium.features.GeoJsonTooltip(
            fields=['geoAreaName', 'latest_value'],
            aliases=['País (Área geográfica): ', 'Prevalência de desnutrição (%): '],
            style="background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;",
            localize=True)
    ).add_to(m)
    folium.LayerControl().add_to(m)
    folium_static(m)

    pol_par = hunger.groupby("parentName")[['latest_value']].sum().reset_index()
    pol_par1 = hunger.groupby("geoAreaName")[['latest_value']].sum().reset_index()

    filepath = gpd.read_file(
        "https://services7.arcgis.com/gp50Ao2knMlOM89z/arcgis/rest/services/AG_PRD_FIESSIN_2_1_2_2020Q2G03/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson")

    st.subheader('Porcentagem de subnutrição por região')
    fig = px.bar(x=pol_par['parentName'],
                 y=pol_par['latest_value'],
                 orientation='v',
                 labels={'x': 'Região geográfica', 'y': 'Prevalência de subnutrição por país (%)'},
                 width=900, height=600)
    st.plotly_chart(fig)

    crop = pol_par['parentName']
    fig = px.pie(pol_par, values="latest_value", names="parentName", **COMMON_ARGS)
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    chart(fig)

    df_mask = filepath['sex_desc'] != 'Both sexes'
    filtered_df = filepath[df_mask]

    df_mask1 = filepath['age_desc'] == '15 years old and over'
    filtered_df1 = filepath[df_mask1]

    st.subheader('Prevalência de subnutrição por sexo')
    st.write('Analisando a proporção de pessoas que se encontram em situação de subnutrição, percebe-se que o número de mulheres nessas condições é maior do que de homens, em um panorama geral dos países.')
    crop = filtered_df['sex_desc']
    fig = px.pie(filtered_df, values="latest_value", names="sex_desc", **COMMON_ARGS)
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    chart(fig)
    st.write('**OBS:** Os valores de referência são para pessoas com 15 anos completos ou mais.')

    st.subheader('Fonte dos dados:')
    st.info("""
            \n 🔍 Divisão de Estatística das Nações Unidas [UN DESA Statistics Division](https://unstats.un.org/sdgs/dataportal)""")
