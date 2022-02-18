import streamlit as st

from multipage import MultiPage

from pages.another import another_page
from pages.home import home_page

app = MultiPage()

# Add all your pages here
app.add_page("Home page", home_page)
app.add_page("Another page", another_page)

# Add the main content
st.title("Demo multipage app")
st.write('*the content from `main.py` is shown on every page*')

app.run()
