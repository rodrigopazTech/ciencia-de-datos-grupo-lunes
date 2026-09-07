import pandas as pd
import numpy as np

# Cargar dataset de la carpeta recursos
df_ventas = pd.read_csv("recursos/ventas_ecommerce.csv")

print("==========================================================")
print("   CLASE PRACTICA: LIMPIEZA Y FILTRADO AVANZADO (PANDAS)")
print("==========================================================\n")

# 1. Diagnóstico de Nulos
print("1. DIAGNÓSTICO DE VALORES NULOS:")
print(df_ventas.isna().sum())
print("-" * 50)

# 2. Imputación y Limpieza de Nulos
print("\n2. APLICANDO IMPUTACIÓN Y LIMPIEZA...")
df_ventas["Metodo_Pago"] = df_ventas["Metodo_Pago"].fillna("No Especificado")
df_limpio = df_ventas.dropna(subset=["Estado"]).copy()

print("Nulos restantes tras limpieza:")
print(df_limpio.isna().sum())
print("-" * 50)

# 3. Detección y Eliminación de Duplicados
print("\n3. LIMPIEZA DE DUPLICADOS:")
print(f"Dimensiones iniciales: {df_limpio.shape}")
print(f"Filas duplicadas encontradas: {df_limpio.duplicated().sum()}")

df_sin_duplicados = df_limpio.drop_duplicates().copy()
print(f"Dimensiones finales sin duplicados: {df_sin_duplicados.shape}")
print("-" * 50)

# 4. Filtrado Condicional Complejo con .loc
print("\n4. FILTRADO CONDICIONAL CON .loc[]:")
filtro_alta_gama = df_sin_duplicados.loc[
    (df_sin_duplicados["Categoria"] == "Electrónica") & (df_sin_duplicados["Precio_Unitario"] >= 10000),
    ["ID_Pedido", "Producto", "Precio_Unitario", "Ciudad"]
]

print("Ventas de Electrónica >= $10,000:")
print(filtro_alta_gama.head(10))
print(f"\nTotal registros que cumplen la condición: {len(filtro_alta_gama)}")
print("==========================================================")
