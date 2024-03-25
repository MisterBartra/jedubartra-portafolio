import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import altair as alt
import time
import zipfile

active_button=False

def desactivable_button():
    if (st.button("Desactivar sección") and active_button):
        active_button=False
    else:
        active_button=True

# Page title
st.set_page_config(page_title='Resume - José Eduardo Bartra Quispe', page_icon='0')

# Título y descripción
st.title("José Eduardo Bartra Quispe")
st.markdown("## Acerca de mí")
st.markdown("Me presento siendo desarrollador con experiencia de Java con una pasión por explorar nuevas tecnologías. Desde 2014, trabajé editando variedad de juegos haciendo mis versiones de los mismos, más ligeros en la carga de recursos ya sea desde el codigo json hasta los archivos multimedia, explorando lo que recopila en su funcionamiento y realizando cambios. Me especializo en Java y Excel, y ví en Python una herramienta más sencilla de manejar para crear herramientas útiles en análisis de datos y la optimización.")
st.markdown("Comparto el [repositorio de juegos](https://www.mediafire.com/folder/0c3orz3r4nv3n/Juegos) que tengo subido hasta el momento")

# Botones para cambiar la información
st.title("Experiencia")
#if st.button("Experience"):
    # Experiencia y habilidades
st.markdown("## Experiencia y Calificaciones")
st.markdown("Tengo 10 años de experiencia en sintaxis y programación en Java haciendo manejo de hilos, puedo afimar mi buena comprensión gracias a mi estudio autonomo y veo Python para realizar cómodo de mis bots de asistencia de apoyo especifico en dar dirección los datos ingresados así como bots totalmente independientes. Asu vez, era una opción distinta a desempeñar mis conocimientos para la construcción herramientas que optimizan y agilizan las tareas para el manejo de información.")
st.markdown("## Habilidades Técnicas")
st.markdown("- **Lenguajes**: Excel, Python, Office, Git, SQL & Github")

    # Educación reciente
st.markdown("## Educación Reciente")
st.markdown("- **Aplicación de Node.js para Bots**: Creación de herramientas de programación automática en Python en oficio de hacer mas cosas | 05/2023 – actualidad")
st.markdown("- **Diploma en Diseño/Desarrollo de Videojuegos**: Instituto San Ignacio de Loyola, Miraflores, Perú | 03/2021 – 12/2023")

    #desactivable_button()

st.title("Proyectos")
#elif st.button("Education") or active_button:
    #excel = st.radio("Hojas:", ["Desactivado", "Experiencias en Excel"])
    # Proyecto Exploratorio: Juegos y Prototipos
    #st.image("https://img.itch.zone/aW1nLzc2Mjk0MzAucG5n/315x250%23c/vpsaRo.png", use_column_width=True)
    # Botones para cambiar la información
    #option = st.radio("Selecciona una sección:", ["Experiencias en Excel", "Juego - Caught we one", "Puntero celdas a Notas", "Platilla de recorrido por bot", "Cortes de datos y funciones complejas entre hojas"])
    #if option == "Juego - Caught we one":
st.markdown("### Proyecto Exploratorio: Juego y Bots de autonomía")
    #elif option == "Experiencias en Excel":
st.markdown("Puntero celdas a Notas")
st.components.v1.iframe("https://docs.google.com/spreadsheets/d/1oM_05TjsT-wHYQ_mYyyG9xGaj3fqATJB_Z1Qfg0oEJQ/edit#gid=0&range=G4", height=600)
        #if option == "Puntero celdas a Notas":
st.markdown("Proyecto de Carrera:") 
st.components.v1.iframe("https://html-classic.itch.zone/html/4908231/index.html", height=320)
        #elif option == "Platilla de recorrido por bot":
st.markdown("Hoja en plan de recorrido de mi bot:") 
st.components.v1.iframe("https://docs.google.com/spreadsheets/d/11qVrrLPXXvmh8jLqE1gh7nkepN2VFZYl/edit#gid=241212179&range=I14", height=800)
        #elif option == "Cortes de datos y funciones complejas entre hojas":
st.markdown("Cortes de datos y funciones complejas entre hojas:")
st.components.v1.iframe("https://docs.google.com/spreadsheets/d/1Cdb9clJcJiW4RW8VJADKgqILcfFj9Xlx/edit#gid=1458070952&range=S194", height=800)
    
    #desactivable_button()
    
st.title("Contacto")
#elif st.button("Contact"):
    # Información de contacto
st.markdown("## Información de Contacto")
st.markdown("- **Email:\n[jedubartra21@gmail.com](mailto:jedubartra21@gmail.com)**")
st.markdown("- **[LinkedIn](https://www.linkedin.com/in/jose-eduardo-bartra-quispe-jedubartra-9563991b5/)**")
st.markdown("- **[GitHub](https://github.com/misterbartra/)**")
   
    #desactivable_button()
    
