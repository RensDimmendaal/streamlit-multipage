import streamlit as st

class MultiPage: 
    """Framework for combining multiple streamlit applications."""

    def __init__(self) -> None:
        self.pages = dict()

    
    def add_page(self, page_title, page_func) -> None: 
        self.pages[page_title] = page_func

    def run(self):
        page_title = st.sidebar.selectbox(
            'Page Navigation', 
            list(self.pages.keys()), 
        )

        self.pages[page_title]()
