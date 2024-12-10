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
import pathlib

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

# ---------------- Configuracion CSS --------------------------

def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

css_path = pathlib.Path("assets/style.css")
load_css(css_path)

# --------------------------- Code ---------------------------

st.markdown("<div class='titulo'><h1 class='creditos'>Creditos.</h1></div>", unsafe_allow_html=True)

st.divider()

st.markdown(
    """
    ### :green[:material/grid_view:] Diseño de UI
    :green[**Página principal**]  
    * Alan Torres Ruiz  
    * Paola Montserrat Osorio García  

    :green[**Interacción con el grafo**]
    
    Creación de estructura base para el desplegado de plano tridimensional con scatter3d Traces de Plotly. Creación, eliminación y edición de nodos y aristas. Menú con deslizadores para manipulación de propiedades (tamaño y color). Íconos para botones.
    * Vanessa Reteguín  
    * Martín Isaí Núñez Villeda  
    ### :blue[:material/account_tree:] Construcción de grafos
    :blue[**Implementación de nodos**]
    * Alexis Alberto Zúñiga Alonso  
    * Pablo David Pérez López  

    :blue[**Implementación de arcos**]  
    * Abel López Rosales  
    * Jesús Yocsan Luévano Flores
    ### :violet[:material/browse_activity:] Funcionamiento de menús
    :violet[**Backend**]
    * Eduardo Isaí Lopez García  
    * Alan Fernando Martinez Moreno  

    :violet[**Administración de archivos**] 
    * Zahid Ríos Durón  
    * Jesús Emmanuel Saucedo Solís
    """
)

st.divider()

st.caption("Derechos reservados de uso para el Equipo 1")
