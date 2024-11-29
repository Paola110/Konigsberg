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
# ------------------------- Variables -------------------------
# Time

# ---------------- Configuracion de la pagina -----------------

st.set_page_config(
    page_title="Konigsberg",
    page_icon="🕸️",
    layout="wide", 
    initial_sidebar_state="auto"
)


# ---------------------- Menu desplegable ---------------------

def menu():
    st.sidebar.page_link("main_konigsberg.py", label="Pagina inicial", icon="🕸️")
    st.sidebar.page_link("pages/Creditos_menu.py", label="Creditos", icon="🗒️")
    st.sidebar.page_link("pages/Enlaces_menu.py", label="Enlaces", icon="🔗")

menu()

# --------------------------- Code ---------------------------

st.title("Konigsberg - :blue[_Grafos_]")

st.subheader("¿Cómo se usa?", divider = "gray")

st.markdown(
    """
    A la izquierda arriba al presionar la flecha se abrira un menu desplegable con dos opciones, enlaces pertinentes al codigo y los creditos donde se podran ver los roles de cada uno de los miembros del equipo. 
    
    Debajo de este apartado se encontraran dos botones, "Crear" donde se podra crear e interactuar con un grafo, y "Cargar" donde se podra abrir un grafo ya creado y guardado para poder interactuar con el.
    """
)

st.divider()

c1, c2 = st.columns(2)

with c1:
    Crear = st.button('Crear grafo', use_container_width=True, type="primary")
with c2:
    Cargar = st.button('Cargar grafo', use_container_width=True, type="secondary")

if Crear:
    st.write('Presionaste el boton')

if Cargar:
    st.write('Presionaste el boton')

st.subheader("Los grafos y su historia", divider = "gray")

c1, c2 = st.columns(2)

with c1:
    st.markdown(
        """
        Un grafo es un conjunto de objetos llamados :orange[_vértices o nodos_] unidos por enlaces llamados :orange[_aristas o arcos_], que permiten representar relaciones binarias entre elementos de un conjunto.

        Prácticamente cualquier problema puede representarse mediante un grafo, y su estudio trasciende a las diversas áreas de las ciencias exactas y las ciencias sociales.        

        Ademas debemos mencionar que existen tres tipos de grafos en cuanto a su direccionalidad, los grafos :orange[_dirigidos_], los grafos :orange[_no dirigidos_] y los grafos :orange[_mixtos_].
        """
    )

with c2:
    with st.container(height=250):
        st.markdown("Grafo")

st.markdown(
    """    
    En cuanto a su historia, la teoría de grafos se remonta al siglo XVIII con el problema de los puentes de :orange[_Königsberg_], el cual consistía en encontrar un camino que recorriera los siete puentes del río Pregel, de modo que se recorrieran todos los puentes pasando una sola vez por cada uno de ellos. El término grafo, proviene de la expresión inglesa graphic notation («notación gráfica»), usada por primera vez por Edward Frankland y posteriormente adoptada por Alexander Crum Brown en 1884 y que hacía referencia a la representación gráfica de los enlaces entre los átomos de una molécula.
    """
)

st.divider()

st.caption("Derechos reservados de uso para el equipo 1")
