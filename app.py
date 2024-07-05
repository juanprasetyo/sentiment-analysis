import streamlit as st
from streamlit_option_menu import option_menu

# Konfigurasi Streamlit
st.set_page_config(page_title="Sentiment Analysis", page_icon=":bar_chart:", layout="wide")

# Navbar
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Prediksi Sentimen"],
        icons=["house", "graph-up"],
        menu_icon="cast",
        default_index=0,
    )

# Import halaman
if selected == "Home":
    from page import home
    home.show()

if selected == "Prediksi Sentimen":
    from page import sentiment_analysis
    sentiment_analysis.show()
