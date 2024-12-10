# +----------------------------------------------------------------------------+
# | Konigsberg v1.0.0
# +----------------------------------------------------------------------------+
# | Authors:
# | Martín Isaí Nuñez  <>
# | Vanessa Reteguín   <vanessa@reteguin.com>
# | Released under the MIT license
# +----------------------------------------------------------------------------+
# | First release: November 29th, 2024
# | Last update..: December 2nd, 2024
# | WhatIs.......: Crear_grafo.py - Konigsberg
# +----------------------------------------------------------------------------+

# Run: streamlit run /Users/vanessa/VS_Code/Python/main_konigsberg.py                                   

# ------------ Resources / Documentation involved -------------
# Streamlit API reference: https://docs.streamlit.io/develop/api-reference

# Python Figure Reference: scatter3d Traces: https://plotly.com/python/reference/scatter3d/

# ------------------------- Libraries -------------------------
import streamlit as st
import plotly.graph_objects as pl
import os
import json

# ------------------------- Variables -------------------------
graphGridHeight = 800
image_dir = 'static' # directorio de imágenes

# --------------------------- Code ---------------------------

# ---------------------- Menu desplegable ----------------------

def menu():
    st.sidebar.page_link("main_konigsberg.py", label="Pagina principal", icon="🕸")
    st.sidebar.page_link("pages/Crear_grafo.py", label="Crear grafo", icon="✏")
    st.sidebar.page_link("pages/Creditos_menu.py", label="Creditos", icon="🗒")
    st.sidebar.page_link("pages/Enlaces_menu.py", label="Enlaces", icon="🔗")
menu()

# campo de entrada para el título del gráfico
graph_title = st.text_input("Título del Gráfo", "Inserte nombre de grafo aquí")

st.title(graph_title)

# Listas para almacenar nodos y aristsdr
if 'nodos' not in st.session_state:
    st.session_state['nodos'] = []

if 'aristas' not in st.session_state:
    st.session_state['aristas'] = []

# Estado de las herramientsda
if 'mostrar_formulario' not in st.session_state:
    st.session_state['mostrar_formulario'] = {'add_node': False, 'move_node': False, 'add_edge': False, 'customize': False, 'load_node': False, 'save_node': False}
else:
    # Asegurarse de que todas las claves esatn presentes
    if 'customize' not in st.session_state['mostrar_formulario']:
        st.session_state['mostrar_formulario']['customize'] = False
    if 'load_node' not in st.session_state['mostrar_formulario']:
        st.session_state['mostrar_formulario']['load_node'] = False
    if 'save_node' not in st.session_state['mostrar_formulario']:
        st.session_state['mostrar_formulario']['save_node'] = False

query_params = st.query_params

# Verificamos si la página es 'Crear_grafo' y si el parámetro 'load' está presente
if query_params.get("load", [None])[0] == "true":
    # Cambiar el estado del formulario
    for k in st.session_state['mostrar_formulario']:
        st.session_state['mostrar_formulario'][k] = False  # Desactivar todos los formularios
    st.session_state['mostrar_formulario']['load_node'] = True  # Activar el formulario de carga
    st.experimental_rerun()

fig = pl.Figure()
fig.update_layout(height=graphGridHeight)

fig.update_layout(scene=dict(
    xaxis_title='X AXIS',
    yaxis_title='Y AXIS',
    zaxis_title='Z AXIS'
))

# Crear dos filas para los iconos y las opciones
cols1 = st.columns([1, 1, 1])
cols2 = st.columns([1, 1, 1])

# Funcion para mostrar botones con imágenes y texto
def mostrar_boton(contenedor, titulo, imagen, estado, clave):
    if contenedor.button(titulo, key=clave):
        for k in st.session_state['mostrar_formulario']:
            st.session_state['mostrar_formulario'][k] = False
        st.session_state['mostrar_formulario'][estado] = True
    contenedor.image(os.path.join(image_dir, imagen), width=120)

# Primera fila de iconos
mostrar_boton(cols1[0], "Nuevo nodo", 'n_nodo.jpg', 'add_node', 'boton_nuevo_nodo')
mostrar_boton(cols1[1], "Modificar nodo", 'M_nodo.jpg', 'move_node', 'boton_mover_nodo')
mostrar_boton(cols1[2], "Modificar aristas", 'A_arista.jpg', 'add_edge', 'boton_añadir_arista')

# Segunda fila de iconos
mostrar_boton(cols2[0], "Personalizar", 'p_nodo.jpg', 'customize', 'boton_personalizar')
mostrar_boton(cols2[1], "Cargar", 'c_grafo.jpg', 'load_node', 'boton_cargar')
mostrar_boton(cols2[2], "Guardar", 'g_graph.jpg', 'save_node', 'boton_guardar')

# Función para verificar si una arista ya existe
def arista_ya_existe(node1, node2):
    for arista in st.session_state['aristas']:
        if (arista["node1"]["name"] == node1 and arista["node2"]["name"] == node2) or \
           (arista["node1"]["name"] == node2 and arista["node2"]["name"] == node1):
            return True
    return False
    
# Mostrar el formulario correspondiente segun la herramienta seleccionada
if st.session_state['mostrar_formulario']['add_node']:
    with st.form(key='add_node_form'):
        node_name = st.text_input("📌 Nombre del Nodo")
        
        col_x_text, col_x_slider = st.columns([1, 3])
        with col_x_text:
            node_x_text = st.text_input("Posición en X", value="0")
        with col_x_slider:
            node_x_slider = st.slider("", min_value=-10, max_value=10, value=int(node_x_text), key='slider_node_x')

        col_y_text, col_y_slider = st.columns([1, 3])
        with col_y_text:
            node_y_text = st.text_input("Posición en Y", value="0")
        with col_y_slider:
            node_y_slider = st.slider("", min_value=-10, max_value=10, value=int(node_y_text), key='slider_node_y')

        col_z_text, col_z_slider = st.columns([1, 3])
        with col_z_text:
            node_z_text = st.text_input("Posición en Z", value="0")
        with col_z_slider:
            node_z_slider = st.slider("", min_value=-10, max_value=10, value=int(node_z_text), key='slider_node_z')

        submit_node = st.form_submit_button("Agregar Nodo")

        if submit_node:
            if node_name == "":
                st.warning('Agrege nombre para nuevo nodo', icon="⚠")
            else:
                node_x = node_x_slider if st.session_state.slider_node_x != int(node_x_text) else int(node_x_text)
                node_y = node_y_slider if st.session_state.slider_node_y != int(node_y_text) else int(node_y_text)
                node_z = node_z_slider if st.session_state.slider_node_z != int(node_z_text) else int(node_z_text)

                st.session_state['nodos'].append({
                    "name": node_name,
                    "x": node_x,
                    "y": node_y,
                    "z": node_z
                })

elif st.session_state['mostrar_formulario']['move_node'] and len(st.session_state['nodos']) > 0:
    with st.form(key='move_node_form'):
        selected_node = st.selectbox("🔄 Seleccionar Nodo para Mover", options=[nodo["name"] for nodo in st.session_state['nodos']])
        
        col_x_text, col_x_slider = st.columns([1, 3])
        with col_x_text:
            new_x_text = st.text_input("Nueva Posición en X", value="0")
        with col_x_slider:
            new_x_slider = st.slider(" ", min_value=-10, max_value=10, value=int(new_x_text), key='slider_new_x')

        col_y_text, col_y_slider = st.columns([1, 3])
        with col_y_text:
            new_y_text = st.text_input("Nueva Posición en Y", value="0")
        with col_y_slider:
            new_y_slider = st.slider(" ", min_value=-10, max_value=10, value=int(new_y_text), key='slider_new_y')

        col_z_text, col_z_slider = st.columns([1, 3])
        with col_z_text:
            new_z_text = st.text_input("Nueva Posición en Z", value="0")
        with col_z_slider:
            new_z_slider = st.slider(" ", min_value=-10, max_value=10, value=int(new_z_text), key='slider_new_z')

        submit_move_node = st.form_submit_button("Mover Nodo")

        if submit_move_node:
            new_x = new_x_slider if st.session_state.slider_new_x != int(new_x_text) else int(new_x_text)
            new_y = new_y_slider if st.session_state.slider_new_y != int(new_y_text) else int(new_y_text)
            new_z = new_z_slider if st.session_state.slider_new_z != int(new_z_text) else int(new_z_text)

            for nodo in st.session_state['nodos']:
                if nodo["name"] == selected_node:
                    nodo["x"] = new_x
                    nodo["y"] = new_y
                    nodo["z"] = new_z

        # Añadir botom de eliminación de nodo
        eliminar_nodo = st.form_submit_button("Eliminar Nodo")
        if eliminar_nodo:
            st.session_state['nodos'] = [nodo for nodo in st.session_state['nodos'] if nodo["name"] != selected_node]
            st.session_state['aristas'] = [arista for arista in st.session_state['aristas'] if arista["node1"]["name"] != selected_node and arista["node2"]["name"] != selected_node]

elif st.session_state['mostrar_formulario']['add_edge'] and len(st.session_state['nodos']) > 1:
    with st.form(key='add_edge_form'):
        node1 = st.selectbox("🌐 Seleccionar Nodo 1", options=[nodo["name"] for nodo in st.session_state['nodos']])
        node2 = st.selectbox("🌐 Seleccionar Nodo 2", options=[nodo["name"] for nodo in st.session_state['nodos'] if nodo["name"] != node1])
        edge_weight = st.slider("Peso de la Arista", min_value=1, max_value=20, value=10)
        submit_edge = st.form_submit_button("Agregar Arista")

        if submit_edge:
            if arista_ya_existe(node1, node2):
                st.warning('La arista entre estos nodos ya existe', icon="⚠️")
            else:
                nodo1_data = next(nodo for nodo in st.session_state['nodos'] if nodo["name"] == node1)
                nodo2_data = next(nodo for nodo in st.session_state['nodos'] if nodo["name"] == node2)
                st.session_state['aristas'].append({
                    "node1": nodo1_data,
                    "node2": nodo2_data,
                    "weight": edge_weight
                })
                st.success(f"Arista añadida: {node1} ↔ {node2} con peso {edge_weight}")


        # Añadir boton de eliminación de arista
        eliminar_arista = st.form_submit_button("Eliminar Arista")
        if eliminar_arista:
            st.session_state['aristas'] = [
                arista for arista in st.session_state['aristas']
                if not ((arista["node1"]["name"] == node1 and arista["node2"]["name"] == node2) or
                        (arista["node1"]["name"] == node2 and arista["node2"]["name"] == node1))
            ]
            st.success(f"Arista eliminada entre {node1} y {node2}")

elif st.session_state['mostrar_formulario']['customize']:
    with st.form(key='customize_form'):
        marker_color = st.color_picker("Color del Nodo", value='#0000FF')
        marker_size = st.slider("Tamaño del Nodo", min_value=5, max_value=20, value=10)
        line_color = st.color_picker("Color de la Arista", value='#800080')
        line_width = st.slider("Ancho de la Arista", min_value=1, max_value=20, value=10)
        submit_customize = st.form_submit_button("Personalizar")

        if submit_customize:
            st.session_state['customization'] = {
                "marker_color": marker_color,
                "marker_size": marker_size,
                "line_color": line_color,
                "line_width": line_width
            }

elif st.session_state['mostrar_formulario']['save_node']:
    if st.session_state['nodos'] or st.session_state['aristas']:
        graph_data = {
            "nodos": st.session_state['nodos'],
            "aristas": st.session_state['aristas']
        }
        graph_json = json.dumps(graph_data, indent=4)
        st.download_button(label="Descargar Grafo", data=graph_json, file_name=f"{graph_title}.json")
    else:
        st.warning("No hay datos para guardar", icon="⚠")

elif st.session_state['mostrar_formulario']['load_node']:
    with st.form(key='load_node_form'):
        uploaded_file = st.file_uploader("Cargar Grafo", type=["json"])
        submit_load = st.form_submit_button("Cargar Grafo")

        if submit_load and uploaded_file is not None:
            graph_data = json.load(uploaded_file)
            st.session_state['nodos'] = graph_data["nodos"]
            st.session_state['aristas'] = graph_data["aristas"]

# Mostrar nodos
for nodo in st.session_state['nodos']:
    fig.add_trace(pl.Scatter3d(
        x=[nodo["x"]],
        y=[nodo["y"]],
        z=[nodo["z"]],
        mode='markers',
        marker=dict(
            size=st.session_state.get('customization', {}).get("marker_size", 10),
            color=st.session_state.get('customization', {}).get("marker_color", 'blue')
        ),
        hovertext=nodo["name"],
        hoverinfo="text"
    ))

# Mostrar aristas
for arista in st.session_state['aristas']:
    fig.add_trace(pl.Scatter3d(
        x=[arista["node1"]["x"], arista["node2"]["x"]],
        y=[arista["node1"]["y"], arista["node2"]["y"]],
        z=[arista["node1"]["z"], arista["node2"]["z"]],
        mode='lines',
        line=dict(
            width=st.session_state.get('customization', {}).get("line_width", arista["weight"]),
            color=st.session_state.get('customization', {}).get("line_color", 'purple')
        ),
        hovertext="Arista",
        hoverinfo="text",
        hovertemplate = f"Arista: {arista['weight']}"
    ))

st.plotly_chart(fig)
