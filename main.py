from fastapi import FastAPI, UploadFile, File, Form
import pandas as pd
from sklearn.linear_model import LinearRegression

app = FastAPI(title="API Predictiva Dinámica")

@app.post("/predecir")
async def predecir(meses_futuro: int = Form(...), archivo: UploadFile = File(...)):
    # 1. Leer el archivo CSV que envió el cliente desde el frontend
    df = pd.read_csv(archivo.file)
    df['indice_tiempo'] = pd.to_datetime(df['indice_tiempo'])
    
    # 2. Procesamiento de datos
    df_final = df[['indice_tiempo', 'salon_ventas', 'canales_on_line']].copy()
    df_final['ventas_totales'] = df_final['salon_ventas'] + df_final['canales_on_line']
    df_final['porcentaje_online'] = (df_final['canales_on_line'] / df_final['ventas_totales']) * 100
    df_final['mes_numero'] = range(1, len(df_final) + 1)
    
    # 3. Entrenamiento del modelo al vuelo
    X = df_final[['mes_numero']]
    y = df_final['porcentaje_online']
    modelo = LinearRegression()
    modelo.fit(X, y)
    
    # 4. Proyección
    mes_proyectado = len(df_final) + meses_futuro
    fecha_proyectada = df_final['indice_tiempo'].max() + pd.DateOffset(months=meses_futuro)
    
    df_prediccion = pd.DataFrame({'mes_numero': [mes_proyectado]})
    resultado = modelo.predict(df_prediccion)
    
    return {
        "fecha_proyectada": f"{fecha_proyectada.month}/{fecha_proyectada.year}",
        "porcentaje_online_estimado": round(resultado[0], 2)
    }