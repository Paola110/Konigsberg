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
    page_title="Creditos - Autores",
    page_icon="🗒️",
    layout="wide", 
    initial_sidebar_state="auto"

)

menu()

# --------------------------- Code ---------------------------

st.title("Creditos")

st.markdown(
    """
    ## Tareas realizadas por cada integrante del equipo
    "Nombre" fue responsable del area de "area", realizando la tarea de "tarea"
    """
)