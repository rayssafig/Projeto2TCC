"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st

# app_state = st.experimental_get_query_params()
# app_state = {k: v[0] if isinstance(v, list) else v for k, v in app_state.items()} # fetch the first item in each query string as we don't have multiple values for each query string key in this example


class MultiApp:
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({"title": title, "function": func})

    def run(self):
        app_state = st.experimental_get_query_params()
        app_state = {
           # k: v[0] if isinstance(v, list) else v for k, v in app_state.items()
        }  # fetch the first item in each query string as we don't have multiple values for each query string key in this example

        # st.write('before', app_state)

        titles = [a["title"] for a in self.apps]
        functions = [a["function"] for a in self.apps]
        default_radio = titles.index(
            app_state["page"]) if "page" in app_state else 0

        st.sidebar.title("Menu dos painéis")
        title = st.sidebar.radio(
            'Selecione o ODS:',
            ['Home', 'Erradicação da pobreza', 'Fome Zero e Agricultura Sustentável', 'Saúde e Bem-Estar'], )

        if title == 'Home':
            st.markdown('## Bem-vindo a essa aplicação!')

        elif title == 'Erradicação da pobreza':
            st.markdown('## Erradicar a pobreza em todas as formas e em todos os lugares')

        elif title == 'Fome Zero e Agricultura Sustentável':
            st.markdown(
                '## Erradicar a fome, alcançar a segurança alimentar, melhorar a nutrição e promover a agricultura sustentável')

        elif title == 'Saúde e Bem-Estar':
            st.markdown(
                '## Garantir o acesso à saúde de qualidade e promover o bem-estar para todos, em todas as idades')


        # Check if 'key' already exists in session_state
        # If not, then initialize it
        if 'key' not in st.session_state:
            st.session_state['key'] = 'value'

        # Session State also supports the attribute based syntax
        if 'key' not in st.session_state:
            st.session_state.key = 'value'

        #app_state["page"] = st.session_state.radio
        # st.write('after', app_state)

        #st.experimental_set_query_params(**app_state)
        # st.experimental_set_query_params(**st.session_state.to_dict())
        #functions[titles.index(title)]()

        st.sidebar.title("Sobre")
        st.sidebar.info(
            "Essa aplicação é um projeto open-source disponínel no [GitHub](https://github.com/rayssafig/Projeto2TCC) mantida por Rayssa Figueiredo")
