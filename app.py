import streamlit as st 
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("Proyección de Ventas: Salón vs Online")
archivo_subido = st.file_uploader("Cargar archivo CSV", type=["csv"])

if archivo_subido is not None:
    df = pd.read_csv(archivo_subido)
    columnas_requeridas = ["salon_ventas", "canales_on_line"]
    
    if all(col in df.columns for col in columnas_requeridas):
        st.success("Archivo válido. Columnas encontradas.")
        st.dataframe(df.head())
        
        # --- Procesamiento de Datos (AQUÍ ADENTRO) ---
        
        # 1. Preparación de variables
        df_final = df[['indice_tiempo', 'salon_ventas', 'canales_on_line']].copy()
        
        # ¡IMPORTANTE! Convertimos la columna a formato fecha
        df_final['indice_tiempo'] = pd.to_datetime(df_final['indice_tiempo'])
        
        df_final['ventas_totales'] = df_final['salon_ventas'] + df_final['canales_on_line']
        df_final['porcentaje_online'] = (df_final['canales_on_line'] / df_final['ventas_totales']) * 100
        df_final['mes_numero'] = range(1, len(df_final) + 1)
                
        st.write("Datos procesados (Porcentaje Online):")
        st.dataframe(df_final[['indice_tiempo', 'porcentaje_online', 'mes_numero']].head())
                
        # 2. Entrenamiento del Modelo
        X = df_final[['mes_numero']]
        y = df_final['porcentaje_online']
                
        modelo = LinearRegression()
        modelo.fit(X, y)
                
        st.success("Modelo entrenado con éxito.")
        st.write(f"Crecimiento promedio mensual estimado: **{modelo.coef_[0]:.3f}%**")

        # 3. Simulador Interactivo
        st.subheader("Simulador de Escenarios para Logística")
        st.write("Proyecte el porcentaje de ventas online para los próximos meses.")
                
        meses_futuro = st.slider("¿Cuántos meses a futuro desea proyectar?", min_value=1, max_value=24, value=10)
                
        if st.button("Calcular Proyección"):
            # 1. Calculamos el mes numérico para el modelo
            mes_proyectado = len(df_final) + meses_futuro
            
            # 2. Calculamos la fecha calendario para el usuario
            ultima_fecha = df_final['indice_tiempo'].max()
            fecha_proyectada = ultima_fecha + pd.DateOffset(months=meses_futuro)
            fecha_texto = f"{fecha_proyectada.month}/{fecha_proyectada.year}"
            
            # 3. Predicción
            df_prediccion = pd.DataFrame({'mes_numero': [mes_proyectado]})
            resultado = modelo.predict(df_prediccion)
            
            st.info(f"Proyección ({fecha_texto}): En {meses_futuro} meses, las ventas online representarán aproximadamente el **{resultado[0]:.2f}%** del total.")
            st.write("Esta métrica permite justificar la reasignación preventiva de personal del salón hacia el área de envíos.")

    else:
        st.error(f"Error. El archivo debe contener exactamente las columnas: {columnas_requeridas}")