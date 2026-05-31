import streamlit as st 
import pandas as pd
import requests

st.title("Proyección de Ventas: Salón vs Online")
archivo_subido = st.file_uploader("Cargar archivo CSV", type=["csv"])

if archivo_subido is not None:
    df = pd.read_csv(archivo_subido)
    columnas_requeridas = ["salon_ventas", "canales_on_line"]
    
    if all(col in df.columns for col in columnas_requeridas):
        st.success("Archivo válido. Columnas encontradas.")
        st.dataframe(df.head())
        
        st.subheader("Simulador de Escenarios para Logística")
        meses_futuro = st.slider("¿Cuántos meses a futuro desea proyectar?", min_value=1, max_value=24, value=10)
                
        if st.button("Calcular Proyección"):
            api_url = "http://127.0.0.1:8000/predecir"
            
            # Preparamos el archivo y los datos para el envío masivo (Multipart)
            archivo_subido.seek(0)
            archivos = {"archivo": (archivo_subido.name, archivo_subido.getvalue(), "text/csv")}
            datos = {"meses_futuro": meses_futuro}
            
            try:
                # Enviamos el archivo real a la API
                respuesta = requests.post(api_url, files=archivos, data=datos)
                
                if respuesta.status_code == 200:
                    datos_api = respuesta.json()
                    st.info(f"Proyección ({datos_api['fecha_proyectada']}): En {meses_futuro} meses, las ventas online representarán aproximadamente el **{datos_api['porcentaje_online_estimado']}%** del total.")
                    st.write("Esta métrica permite justificar la reasignación preventiva de personal del salón hacia el área de envíos.")
                else:
                    st.error("Error en la respuesta de la API.")
            except Exception as e:
                st.error(f"Error de conexión con el backend: {e}")
    else:
        st.error(f"Error. El archivo debe contener exactamente las columnas: {columnas_requeridas}")