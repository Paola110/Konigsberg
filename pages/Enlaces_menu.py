# +----------------------------------------------------------------------------+
# | Konigsberg v1.0.0
# +----------------------------------------------------------------------------+
# | Authors:
# | Alan Torres Ruiz
# | Paola Montserrat Osorio García
# |# +----------------------------------------------------------------------------+
# | First release: November 28th, 2024
# | Last update.: November 28th, 2024
# | WhatIs.......: Konigsberg - Main
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# Title: Link

# ------------------------- Libraries -------------------------
import time  # time.sleep(1)
import streamlit as st
import numpy as np
import pandas as pd
import pathlib

from main_konigsberg import menu
# ------------------------- Variables -------------------------
# Time
# ---------------- Configuracion de la pagina -----------------

st.set_page_config(
    page_title="Enlaces",
    page_icon="🔗",
    layout="wide", 
    initial_sidebar_state="auto"
)

menu()

# ---------------- Configuracion CSS --------------------------

def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

css_path = pathlib.Path("assets/style.css")
load_css(css_path)

# --------------------------- Code ---------------------------

st.markdown("<div class='titulo'><h1 class='enlaces'>Enlaces.</h1></div>", unsafe_allow_html=True)

st.divider()

st.markdown(
    """
    ### :green[:material/link:] Link a la pagina principal
    https://konigsberg.streamlit.app/    
    
    ### :violet[:material/link:] Github
    https://github.com/Paola110/Konigsberg.git

    """
)

st.divider()

st.caption("Derechos reservados de uso para el Equipo 1")
