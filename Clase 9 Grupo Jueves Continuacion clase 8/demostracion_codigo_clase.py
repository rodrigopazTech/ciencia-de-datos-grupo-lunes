import pandas as pd
import numpy as np

# Cargar dataset de la carpeta recursos
df_ventas = pd.read_csv("recursos/ventas_ecommerce.csv")

print("==========================================================")
print("   CLASE PRACTICA: LIMPIEZA Y FILTRADO AVANZADO (PANDAS)")
print("==========================================================\n")

# 1. Diagnóstico de Nulos
# isna() devuelve una máscara booleana (True/False) para indicar qué valores son nulos.
# .sum() sobre esa máscara cuenta cuántos True hay en cada columna, es decir, cuántos nulos tiene cada campo.
print("1. DIAGNÓSTICO DE VALORES NULOS:")
print(df_ventas.isna().sum())
print("-" * 50)

# 2. Imputación y Limpieza de Nulos
print("\n2. APLICANDO IMPUTACIÓN Y LIMPIEZA...")
df_ventas["Metodo_Pago"] = df_ventas["Metodo_Pago"].fillna("No Especificado")
# dropna(subset=["Estado"]) elimina filas donde la columna 'Estado' tiene valores nulos.
# El parámetro subset indica sobre qué columna(s) debe evaluar la presencia de NaN.
# .copy() crea una copia del DataFrame limpio para evitar modificar el original por accidente.
df_limpio = df_ventas.dropna(subset=["Estado"]).copy()

print("Nulos restantes tras limpieza:")
print(df_limpio.isna().sum())
print("-" * 50)

# 3. Detección y Eliminación de Duplicados
# duplicated() devuelve una máscara booleana con True en las filas repetidas.
# .sum() sobre esa máscara cuenta cuántas filas están duplicadas.
print("\n3. LIMPIEZA DE DUPLICADOS:")
print(f"Dimensiones iniciales: {df_limpio.shape}")
print(f"Filas duplicadas encontradas: {df_limpio.duplicated().sum()}")

df_sin_duplicados = df_limpio.drop_duplicates().copy()
print(f"Dimensiones finales sin duplicados: {df_sin_duplicados.shape}")
print("-" * 50)

# 4. Filtrado Condicional Complejo con .loc
# .loc[] permite filtrar por etiquetas/nombres y seleccionar columnas por nombre.
# La parte antes de la coma define las filas: aquí pedimos filas donde la categoría sea 'Electrónica'
# y el precio unitario sea mayor o igual a 10000.
# La parte después de la coma define las columnas a mostrar: ID_Pedido, Producto, Precio_Unitario y Ciudad.
print("\n4. FILTRADO CONDICIONAL CON .loc[]:")
filtro_alta_gama = df_sin_duplicados.loc[
    (df_sin_duplicados["Categoria"] == "Electrónica") & (df_sin_duplicados["Precio_Unitario"] >= 10000),
    ["ID_Pedido", "Producto", "Precio_Unitario", "Ciudad"]
]

print("Ventas de Electrónica >= $10,000:")
print(filtro_alta_gama.head(10))
print(f"\nTotal registros que cumplen la condición: {len(filtro_alta_gama)}")
print("==========================================================")
