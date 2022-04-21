"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
from PIL import Image

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
        app_state = {}

        titles = [a["title"] for a in self.apps]
        functions = [a["function"] for a in self.apps]
        default_radio = titles.index(
            app_state["page"]) if "page" in app_state else 0

        with st.sidebar.container():
            st.title('Cartografia para os ODS')
            image = Image.open("SDG Wheel_PRINT_Transparent.png")
            st.image(image, width=185, use_column_width = False)

        title = st.sidebar.radio(
            "Ir para:", titles, index=default_radio, key="radio")

        app_state["page"] = st.session_state.radio

        st.experimental_set_query_params(**app_state)
        functions[titles.index(title)]()

        st.sidebar.title("Sobre")
        st.sidebar.info(
            """Projeto _Open-Source_ desenvolvido e documentado por [Rayssa Figueiredo](https://github.com/rayssafig)
            \n 🎈 Disponível no [GitHub](https://github.com/rayssafig/Projeto2TCC) 
            \n 💡 Orientação: [Silvana Camboim](https://github.com/SilvanaCamboim)""")

        st.sidebar.title("Instituição")

        st.sidebar.info(
            """🌐 Setor de [Ciência da Terra](http://www.terra.ufpr.br/) 
            \n 💠 Departamento de [Geomática](http://www.geomatica.ufpr.br/)
            \n 🌍 [Eng. Cartográfica e de Agrimensura](http://www.cartografica.ufpr.br/)""")

        st.sidebar.write("[![UFPR](http://www.ufpr.br/portalufpr/wp-content/uploads/2015/11/ufpr_logo.jpg)](https://www.ufpr.br/portalufpr/)")
