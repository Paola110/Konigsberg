# +----------------------------------------------------------------------------+
# | Konigsberg v1.0.0
# +----------------------------------------------------------------------------+
# | Authors:
# | Alan Torres Ruiz
# | Paola Montserrat Osorio García
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
    """
)

st.markdown(
    """
    * **Alan Torres Ruiz**
        <div style="border: 1px solid #d9d9d9; border-radius: 5px; padding: 10px; background-color: rgba(217, 217, 217, 0.2);">
            Implementó el diseño, es decir colores, fuentes, tamaños de letra, forma de los botones, animaciones e imagenes 
            entre otras cosas, de la página principal así como de enlaces y créditos.
        </div>
    * **Paola Montserrat Osorio García**
        <div style="border: 1px solid #d9d9d9; border-radius: 5px; padding: 10px; background-color: rgba(217, 217, 217, 0.2);">
            Implementó la pagina principal dividiendo las secciones que tendria, creo el menu de navegacion, 
            dio el formato que tendrian las paginas, entre otras cosas, de la página principal, enlaces y creditos.
        </div> 


    :green[**Interacción con el grafo**] 
    * **Vanessa Reteguín**
        <div style="border: 1px solid #d9d9d9; border-radius: 5px; padding: 10px; background-color: rgba(217, 217, 217, 0.2);">
            Creación de página y estructura base para el desplegado de plano tridimensional con scatter3d Traces de Plotly, implementación temprana de aristas,
            ademas de la continuación de desarrollo de deslizadores para manipulación de propiedades del grafo.
        </div> 
    * **Martín Isaí Núñez Villeda**
        <div style="border: 1px solid #d9d9d9; border-radius: 5px; padding: 10px; background-color: rgba(217, 217, 217, 0.2);">
            Diseño de iconos de interfaz de usuario para el apartado de interacción de grafos, creación de estructura de botones y 
            espacio 3d de manera base, para posterior implementación, inserción de menu lateral, implementacion de la interacción 
            con titulo de grafo debug temprano del código implementación temprana de aristas y selección de colores para el grafo.
        </div> 
        """,
    unsafe_allow_html=True
)


st.markdown(
    """
    ### :blue[:material/account_tree:] Construcción de grafos
    """,
)

st.markdown(
    """
    :blue[**Implementación de nodos**]
    * **Alexis Alberto Zúñiga Alonso**
        <div style="border: 1px solid #d9d9d9; border-radius: 5px; padding: 10px; background-color: rgba(217, 217, 217, 0.2);">
            Implementó un sistema de etiquetado de nodos que permite diferenciarlos entre sí, además, apoyó en la creación de 
            los modelos 3d de los nodos, y realizó bug fixes a la interfaz.
        </div> 
    * **Pablo David Pérez López**
        <div style="border: 1px solid #d9d9d9; border-radius: 5px; padding: 10px; background-color: rgba(217, 217, 217, 0.2);">
            Participación en la conversión de los nodos de 2D a 3D, al igual que modificaciones en el modelo 3D de forma qué 
            sé pudiera visualizar y manipular de una mejor manera.
        </div> 

    :blue[**Implementación de arcos**]  
    * **Abel López Rosales**
        <div style="border: 1px solid #d9d9d9; border-radius: 5px; padding: 10px; background-color: rgba(217, 217, 217, 0.2);">
            Implementación de la funcion de validacion para las aristas, ademas de ayudar en la implementacion 
            visual de los arcos en la interfaz, entre otras funciones menores.
        </div> 
    * **Jesús Yocsan Luévano Flores**
        <div style="border: 1px solid #d9d9d9; border-radius: 5px; padding: 10px; background-color: rgba(217, 217, 217, 0.2);">
            Implemento la logica de los arcos del grafo en la interfaz grafica, hizo que se mostraran los nombres junto con el peso
            de cada arco, ademas, ayudo para la implementacion de otras partes en la interfaz.
        </div> 
        """,
    unsafe_allow_html=True
)

st.markdown(
    """	

    ### :violet[:material/browse_activity:] Funcionamiento de menús
    """
)

st.markdown(
    """
    :violet[**Backend**]
    * **Eduardo Isaí Lopez García**
        <div style="border: 1px solid #d9d9d9; border-radius: 5px; padding: 10px; background-color: rgba(217, 217, 217, 0.2);">
            Implementó el enlace de los botones a las funciones principales mediante el uso de la funcion nativa "link_button", 
            ademas, ayudo en partes menores o de menor relevancia relacionadas con el backend.
        </div> 
    * **Alan Fernando Martinez Moreno**
        <div style="border: 1px solid #d9d9d9; border-radius: 5px; padding: 10px; background-color: rgba(217, 217, 217, 0.2);">
            Se encargó de realizar las conexiones del archivo main con los demás archivos mediante implementación de hipervínculos 
            donde lo requería y el uso de link_button, concretando así una adecuada navegación entre pestañas
        </div> 

    :violet[**Administración de archivos**] 
    * **Zahid Ríos Durón**
        <div style="border: 1px solid #d9d9d9; border-radius: 5px; padding: 10px; background-color: rgba(217, 217, 217, 0.2);">
            Implementó un módulo que guarda los grafos creados en un archivo JSON, preservando toda la información de nodos, aristas, 
            y sus propiedades. Además, se añade la capacidad de cargar grafos desde archivos JSON, permitiendo a los usuarios recuperar 
            y continuar trabajando con grafos previamente diseñados.
        </div> 
    * **Jesús Emmanuel Saucedo Solís**
        <div style="border: 1px solid #d9d9d9; border-radius: 5px; padding: 10px; background-color: rgba(217, 217, 217, 0.2);">
            Implementó funciones de guardado al grafo en el que se está trabajando, además de una función de cargado de grafos 
            previamente realizados usando un json.
        </div> 
    """, 
    unsafe_allow_html=True
)

st.divider()

st.caption("Derechos reservados de uso para el Equipo 1")
