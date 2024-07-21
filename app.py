import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV en un DataFrame
car_data = pd.read_csv('vehicles_us.csv')

# Mostrar un encabezado con Streamlit
st.header('Exploración de Datos de Vehículos en EE.UU.')

# Crear un botón para construir un histograma
hist_button = st.button('Construir Histograma')

if hist_button:
    # Mostrar un mensaje antes de construir el histograma
    st.write('Construyendo un histograma para el kilometraje de los vehículos')
    
    # Crear el histograma con Plotly Express
    fig_hist = px.histogram(car_data, x='odometer', nbins=50, title='Histograma de Kilometraje')
    
    # Mostrar el histograma interactivo con Streamlit
    st.plotly_chart(fig_hist)

# Agregar otro botón para construir un gráfico de dispersión
scatter_button = st.button('Construir Gráfico de Dispersión')

if scatter_button:
    # Mostrar un mensaje antes de construir el gráfico de dispersión
    st.write('Construyendo un gráfico de dispersión para el precio vs. el año del vehículo')
    
    # Crear el gráfico de dispersión con Plotly Express
    fig_scatter = px.scatter(car_data, x='year', y='price', color='fuelType', title='Precio vs. Año del Vehículo')
    
    # Mostrar el gráfico de dispersión interactivo con Streamlit
    st.plotly_chart(fig_scatter)
