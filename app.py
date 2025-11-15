import streamlit as st

st.header('Lanzar una moneda')
number_of_trails = st.slader('¿Número de intesntos?', 1, 100, 10)
start_button = st.button('Ejecutar')

if start_button: st.write(f'Experimento con {number_of_trails} intentos en curso.')

st.write('Esta aplicación aún no es ficional. En construcción')
