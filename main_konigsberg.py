# +----------------------------------------------------------------------------+
# | Konigsberg v1.0.0
# +----------------------------------------------------------------------------+
# | Authors:
# | Alan Torres      <>
# | Paola Osorio     <> 
# | Vanessa Reteguín <vanessa@reteguin.com>
# +----------------------------------------------------------------------------+
# | First release: November 28th, 2024
# | Last update..: December 2nd, 2024
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
# ------------------------- Variables -------------------------
# Time

# ---------------- Configuracion de la pagina -----------------

st.set_page_config(
    page_title="Konigsberg",
    page_icon="🕸",
    layout="wide", 
    initial_sidebar_state= "collapsed"
)

# -------------------- Configuracion CSS -----------------------

def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

css_path = pathlib.Path("assets/style.css")
load_css(css_path)

# ---------------------- Menu desplegable ----------------------

def menu():
    st.sidebar.page_link("main_konigsberg.py", label="Pagina principal", icon="🕸")
    st.sidebar.page_link("pages/Crear_grafo.py", label="Crear grafo", icon="✏")
    st.sidebar.page_link("pages/Creditos_menu.py", label="Creditos", icon="🗒")
    st.sidebar.page_link("pages/Enlaces_menu.py", label="Enlaces", icon="🔗")

menu()

# --------------------------- Code -----------------------------

st.markdown("<div class='titulo'><h1 class='titulo'>Manipulador de grafos.</h1></div>", unsafe_allow_html=True)

st.markdown("<div class='subtitulo'><h5>Proyecto final de Estructuras Computacionales Avanzadas</h5></div>", unsafe_allow_html=True)

st.divider()

st.markdown("Comienza eligiendo una de las siguientes opciones:")

c1, c2, c3, c4 = st.columns([0.10,0.40,0.40,0.10])

with c2:
    st.image(f"./static/graph_new.png", use_container_width=True)
    st.link_button("Crear grafo", "Crear_grafo", use_container_width=True, icon=":material/note_add:", type="primary") #Boton con interaccion
    #Crear = st.button('Crear grafo', use_container_width=True, icon=":material/note_add:", key="btn_crear") #Boton Original
    
with c3:
    st.image(f"./static/graph_load.png", use_container_width=True)
    st.link_button("Cargar grafo", "/Crear_grafo?load=true", use_container_width=True, icon=":material/file_upload:", type="primary")

    #st.link_button("Cargar grafo", "Crear_grafo", use_container_width=True, icon=":material/file_open:", type="secondary") #Boton con interaccion
    #Cargar = st.button('Cargar grafo', use_container_width=True, icon=":material/file_open:", type="secondary", key="btn_cargar") #Boton Original

#if Crear:
#    st.write('Presionaste el boton Crear')    

#if Cargar:
#    st.write('Presionaste el boton Cargar')

st.write("")

st.markdown("Para más información, revisa la sección :blue[¿Cómo se usa?] debajo. Adicionalmente se encuentra la seccion :violet[*Los grafos y su historia*].")

st.divider()

st.subheader("¿Cómo se usa?", divider= "blue")

st.markdown(
    """
    El proyecto cuenta con las opciones de [Crear](Crear_grafo) o :blue[Cargar] un grafo.  
    * La opción de [:material/note_add: *Crear grafo*](Crear_grafo) inicializa el manipulador de grafos con un espacio vacío.  
    * La opción de :blue[:material/file_open: *Cargar grafo*] necesita de un archivo existente para inicializarlo.    
    
    Funciones del manipulador de grafos:  
    1. Guardar...  
    2. Crear nodo...   
    3. Recorrido...  
    4. ...  
    
        
    Presiona :material/chevron_right: en la esquina superior izquierda para ver los [🗒*Créditos](Creditos_menu) y los [🔗Enlaces*](Enlaces_menu) al código fuente del proyecto.
    """
)

st.subheader("Los grafos y su historia", divider = "violet")

c1, c2 = st.columns(2)

with c1:
    st.markdown(
        """
        Un grafo es un conjunto de objetos llamados :violet[*vértices o nodos] unidos por enlaces llamados :violet[aristas o arcos*], que permiten representar relaciones binarias entre elementos de un conjunto.
        Ademas debemos mencionar que existen tres tipos de grafos en cuanto a su direccionalidad, los grafos :violet[*dirigidos], los grafos :violet[no dirigidos] y los grafos :violet[mixtos*].  
        
        En cuanto a su historia, la teoría de grafos se remonta al siglo XVIII con el problema de los puentes de :violet[Königsberg], el cual consistía en encontrar un camino que recorriera los siete puentes del río Pregel, de modo que se recorrieran todos los puentes pasando una sola vez por cada uno de ellos.  
        El término grafo proviene de la expresión inglesa :violet[graphic notation] («notación gráfica»), usada por primera vez por Edward Frankland y posteriormente adoptada por Alexander Crum Brown en 1884 y que hacía referencia a la representación gráfica de los enlaces entre los átomos de una molécula.  
          
        :violet[*Prácticamente cualquier problema puede representarse mediante un grafo*], y su estudio trasciende a las diversas áreas de las ciencias exactas y las ciencias sociales.  
        """
    )


with c2:
    cardUpperPart = '''
        <div class='cardborder'>
            <div class='container'>
                <h5 style="padding-bottom:0px;">Problema de Königsberg representado por un grafo</h5>
            </div>
        </div>
    '''
    # Favor de no mover el padding ni intentar insertar imagen en contenedor
    # (Streamlit maneja que las imágenes lleguen al navegador y por eso nunca va a llegar desde un <img> tag)

    st.markdown(cardUpperPart, unsafe_allow_html=True)
    st.image(f"static/graph_bridges.png", use_container_width=True)

st.divider()

st.caption("Derechos reservados de uso para el Equipo 1")