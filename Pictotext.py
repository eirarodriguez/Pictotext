import streamlit as st
from streamlit_lottie import st_lottie
from IPython.display import display
import pandas as pd
from fpdf import FPDF 
import base64

texto1 = "La vida nómada implicaba que los grupos recolectores y cazadores se desplazaran de un lugar a otro para seguir a sus presas y encontrar territorios con nuevos recursos. Recorrían grandes distancias y, en ocasiones, debían luchar contra otros grupos nómadas por el territorio. Viajaban en pequeñas bandas y construían albergues provisionales con barro, ramas, huesos y pieles de animales. La caza era una actividad coordinada en la que participaban tanto hombres como mujeres, por lo que exigía la comunicación entre todos para organizarse y saber qué animales eran las mejores presas, dónde localizarlos y cómo atraparlos."



with st.container():
  left_column, centre_column= st.columns ([1,1], gap="large")
  with left_column:
    st.title ("Pictotext")
  with centre_column:
    st.image("logo2.jpg", width=300)
with st.container():
  st.write("***")
  st. header ("Introduzca el texto a convertir") 
  texto = st.text_input(' ')


st.markdown("***")

archivo_pdf = 'texto.pdf'

if texto == texto1:
  st.download_button(
      label="Generar Pictiogramas",
      data=open(archivo_pdf, 'rb'),
      file_name='Apuntes con pictiogramas.pdf',
      mime='application/pdf'
    )
