# +----------------------------------------------------------------------------+
# | Konigsberg v1.0.0
# +----------------------------------------------------------------------------+
# | Authors:
# |
# +----------------------------------------------------------------------------+
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

# --------------------------- Code ---------------------------

st.title("Enlaces")

st.markdown(
    """
    ## Enlaces de interes para el proyecto
    Enlace a "Nombre/Funcion" : [Link]
    """
)