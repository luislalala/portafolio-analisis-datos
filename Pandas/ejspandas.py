# ### EJERCICIO NIVEL BASICO========================================================================
# # Objetivo: Carga, limpieza y exploración básica.
# # Contexto: Dataset de empleados de una empresa.
# # Tareas:
# # Crea un DataFrame con columnas: nombre, departamento, salario, años_experiencia, activo (bool). 
# # Mínimo 20 filas con algunos valores nulos en salario
# # Explora con: .info(), .describe(), .value_counts()
# # Limpia los nulos de salario rellenando con la mediana del departamento correspondiente (.groupby + .transform)
# # Filtra empleados activos con más de 3 años de experiencia
# # Ordena por salario descendente y muestra el top 5
import numpy as np
import pandas as pd
#datos es un diccionario con 
datos = {
    "nombre": [
        "Ana García", "Luis Martínez", "Sofia López", "Carlos Pérez", "María Rodríguez",
        "Juan Hernández", "Valentina Torres", "Diego Flores", "Camila Díaz", "Andrés Morales",
        "Isabella Jiménez", "Miguel Vargas", "Lucía Castro", "Roberto Sánchez", "Daniela Ramos",
        "Fernando Mendoza", "Gabriela Cruz", "Alejandro Reyes", "Natalia Gómez", "Eduardo Ruiz"
    ],
    "departamento": [
        "Ventas", "TI", "RRHH", "Ventas", "Finanzas",
        "TI", "Marketing", "Ventas", "RRHH", "Finanzas",
        "Marketing", "TI", "Ventas", "Finanzas", "Marketing",
        "RRHH", "TI", "Ventas", "Marketing", "Finanzas"
    ],
    "salario": [
        18000, 32000, None, 21000, 28000,
        35000, 24000, None, 19500, 31000,
        26000, None, 22000, 29500, 25000,
        None, 33000, 20000, 27000, 30000
    ],
    "años_experiencia": [
        2, 6, 1, 4, 7,
        9, 3, 1, 2, 8,
        5, 4, 3, 6, 4,
        2, 7, 1, 5, 9
    ],
    "activo": [
        True, True, False, True, True,
        True, True, False, True, True,
        True, True, False, True, True,
        True, True, False, True, True
    ]
}

df = pd.DataFrame(datos) #estamos convirtiendo el diccionario "datos" en una tabla de datos 
datos_no_nulos = df.info() #nos dice la cantidad de filas y columnas, valores no nulos, tipos de datos
resumen = df.describe() #nos da diferentes datos de la tabla std, max, min, mean, etc 
valores_repetidos = df["departamento"].value_counts() #sirve para contar cuántas veces aparece cada valor único en una columna

mediana_dep = df.groupby("departamento")["salario"].transform("median")
#groupby agrupa por datos repetidos en este caso departamento, .transfor calcula mediana, promedio etc. de los datos que agrupamos 
df["salario"] = df["salario"].fillna(mediana_dep) #fillna cambia los datos nulos por el valor que le demos 
#aqui le estamos dando un nuevo valor a salario, en este caso a los valores nulos en la columna salario 
filtro_exp = df[(df["activo"] == True) & (df["años_experiencia"] > 3)] #son los valores que cumplen con las condicones que colocamos 
top_salarios = (filtro_exp
                 .sort_values(by="salario", ascending=False) #sort ordena valores de menor a mayor 
                 .head())  #la los primeros 5 valores 

#=====================================================================================================
# ###EJERCICIO NIVEL INTERMEDIo
# ====================================================================================================
# # Objetivo: GroupBy avanzado, merge y pivot tables.
# # Contexto: Dos datasets: ventas y catálogo de productos.
# # Tareas:
# # Crea df_ventas: fecha (12 meses), region, producto_id, cantidad, descuento
# # Crea df_productos: producto_id, nombre, categoria, precio_unitario
# # Une los DataFrames con merge
# # Calcula ingreso = cantidad * precio_unitario * (1 - descuento)
# # Crea una pivot table: filas=region, columnas=categoria, valores=ingreso total
# # Identifica la región y categoría más rentable cada mes
# # Calcula el crecimiento mes a mes por región (variación porcentual con .pct_change)
datos_ventas = { 
    "fecha": pd.date_range(start="2024-01-01", periods=120, freq="ME"), #rango de tiempo 
    "region": [
        "Norte", "Sur", "Centro", "Occidente", "Oriente",
        "Norte", "Sur", "Centro", "Occidente", "Oriente",
    ] * 12,
    "producto_id": [
        101, 102, 103, 104, 105,
        106, 107, 101, 103, 105,
    ] * 12,
    "cantidad": [
        45, 30, 60, 25, 50,
        35, 40, 55, 20, 65,
    ] * 12,
    "descuento": [
        0.05, 0.10, 0.00, 0.15, 0.05,
        0.10, 0.00, 0.05, 0.20, 0.10,
    ] * 12,
}
datos_productos = {
    "producto_id": [101, 102, 103, 104, 105, 106, 107],
    "nombre": [
        "Laptop Pro", "Mouse Inalámbrico", "Teclado Mecánico",
        "Monitor 4K", "Webcam HD", "Audífonos BT", "Disco SSD"
    ],
    "categoria": [
        "Computadoras", "Accesorios", "Accesorios",
        "Computadoras", "Periféricos", "Audio", "Almacenamiento"
    ],
    "precio_unitario": [18500, 450, 1200, 8900, 1500, 2200, 1800],
}

df_ventas = pd.DataFrame(datos_ventas)
df_productos = pd.DataFrame(datos_productos) #convertimos los diccionarios en bases de datos o tablas 
dt = pd.merge(df_ventas, df_productos) #genera una nueva tabla de datos fusionando las que le damos 
dt["ingreso"] = dt["cantidad"] * dt["precio_unitario"] * (1-dt["descuento"]) #estamos metiendo una nueva columna a la tabla 
#que se calcula con los datos que le damos 
df = dt.pivot_table( #estamos creando una nueva tabla con los datos de otra
    index= "region",
    columns="categoria",
    values= "ingreso",
    aggfunc= "sum"
)
rentabilidad = dt.groupby(["region", "categoria"])["ingreso"].sum() 
#agrupamos por region y categoria y hacenos la suma de los ingresos de cada grupo 
mejor = rentabilidad.idxmax()
print(f"Región y categoría más rentable: {mejor}")

crecimiento = (dt.groupby(["fecha", "region"])["ingreso"]
                 .sum()
                 .unstack("region") #convierte una fila en una columna 
                 .pct_change() * 100) #cambio porcentual de un dato a otro 

# ==========================================================================================================
###EJERCICIO NIVEL AVANZADO 
# ==========================================================================================================
# Datos — genera con np.random un DataFrame con: fecha (año 2024), cliente_id, producto, categoria, precio, cantidad, ciudad, metodo_pago
# Análisis:
# Clientes únicos, ticket promedio, categoría más vendida
# RFM simplificado: calcula Recencia (días desde última compra) y Frecuencia por cliente
# Segmenta clientes en 3 grupos con pd.qcut sobre frecuencia
# Visualización — crea una figura con 4 subplots:

# 📈 Ventas totales por mes (línea)
# 🏆 Top 5 categorías por ingreso (barras horizontales)
# 🎯 Distribución de ticket promedio por ciudad (boxplot)
# 💳 Proporción de métodos de pago (pie chart)
# Presentación: títulos, etiquetas, colores consistentes, tight_layout(), guarda como .png
import matplotlib.pyplot as plt 
import numpy as np
from datetime import datetime 
import pandas as pd 
np.random.seed(42)
n = 500

productos = ["Laptop", "Mouse", "Teclado", "Monitor", "Webcam", "Audífonos", "Disco SSD", "Tablet", "Cámara", "Bocina"]
categorias = {"Laptop": "Computadoras", "Mouse": "Accesorios", "Teclado": "Accesorios",
              "Monitor": "Computadoras", "Webcam": "Periféricos", "Audífonos": "Audio",
              "Disco SSD": "Almacenamiento", "Tablet": "Computadoras", "Cámara": "Periféricos", "Bocina": "Audio"}
precios = {"Laptop": 18500, "Mouse": 450, "Teclado": 1200, "Monitor": 8900, "Webcam": 1500,
           "Audífonos": 2200, "Disco SSD": 1800, "Tablet": 7500, "Cámara": 5500, "Bocina": 3200}
ciudades = ["CDMX", "Guadalajara", "Monterrey", "Puebla", "Tijuana"]
metodos_pago = ["Tarjeta", "Efectivo", "Transferencia", "PayPal"]

productos_lista = np.random.choice(productos, n) #crea un array de 500 elemtos donde hay productos al azar 

datos = {
    "fecha": pd.date_range(start="2024-01-01", periods=n, freq="D").to_series().sample(frac=1, random_state=42).values,
    "cliente_id": np.random.randint(1001, 1201, n),        # 200 clientes únicos posibles
    "producto": productos_lista,
    "categoria": [categorias[p] for p in productos_lista],
    "precio": [precios[p] * np.random.uniform(0.9, 1.1)    # variación ±10% en precio
               for p in productos_lista],
    "cantidad": np.random.randint(1, 5, n), #un array de tamaño n y datos entre 1 y 5
    "ciudad": np.random.choice(ciudades, n), #.choice toma un valor al azar de una lista 
    "metodo_pago": np.random.choice(metodos_pago, n, p=[0.45, 0.25, 0.20, 0.10]),
    #p es la probabilidad de que salga cada valor de metodos de pago .45 en el caso de tarjera, .25 efectivo y asi 
}

df = pd.DataFrame(datos) #convertimos el diccionario de datos en un dataframe 
#las siguientes son nuevas columnas que se van añadir a df 
df["precio"] = df["precio"].round(2) #round redondea para que solo tengas 2 decimales 
df["fecha"] = pd.to_datetime(df["fecha"]) #llena con la fecha del dia 
df["ingreso"] = df["precio"] * df["cantidad"] 

# Clientes únicos — cuántos IDs distintos hay
clientes_unicos = df["cliente_id"].nunique() #nunique nos dice cuantos valores distintos tenemos 

# Ticket promedio — promedio del ingreso por transacción
ticket_promedio = df["ingreso"].mean() #promedio de ingresos 

# Categoría más vendida — cuál categoría sumó más ingreso
categoria_mas_vendida = df.groupby("categoria")["ingreso"].sum().idxmax() #idemax nos dice cual es indice mas alto en este caso la mas vendida

print(f"Clientes únicos: {clientes_unicos}") 
print(f"Ticket promedio: ${ticket_promedio:,.2f}") #:,.2f es para dar formato de moneda 
print(f"Categoría más vendida: {categoria_mas_vendida}")

fecha_max = df["fecha"].max()  # fecha de referencia — el último día del dataset 

#calculo de recencia (cuanto tiempo ha pasado desde el ultimo evento)
rfm = df.groupby("cliente_id").agg( #agg crea nuevas columnas 
    recencia   = ("fecha", lambda x: (fecha_max - x.max()).days), #resta la fecha mas reciente de compra y la resta al dia de hoy 
    frecuencia = ("cliente_id", "count") #cuenta cuantas veces aparece el cliente en la lista
).reset_index()
#Cuando agrupas por cliente_id, Pandas convierte esa columna en el índice (el nombre de las filas).
# Al usar reset_index(), vuelves a convertir al cliente en una columna normal y le asignas números (0, 1, 2...) a las filas

rfm["segmento"] = pd.qcut( #dividimos a los clientes en grupos exactos y les asignamos un nivel dependiendo su posición 
    rfm["frecuencia"], #se ordenan las frecuencias de mayores a menores y luego agrupa de forma equitativa 
    q=3,
    labels=["Bajo", "Medio", "Alto"]
)

# =============================================================================
# PREPARACIÓN DE DATOS PARA CADA SUBPLOT
# =============================================================================

# Subplot 1 — agrupamos por mes (dt.month extrae el número de mes de la fecha)
# y sumamos todos los ingresos de ese mes
ventas_mes = df.groupby(df["fecha"].dt.month)["ingreso"].sum()

# Subplot 2 — agrupamos por categoría y sumamos ingresos
# sort_values(ascending=True) ordena de menor a mayor para que
# las barras horizontales queden con el mayor valor arriba
# tail(5) toma los últimos 5 — los más grandes tras ordenar ascendente
top_categorias = (df.groupby("categoria")["ingreso"]
                    .sum()
                    .sort_values(ascending=True)
                    .tail(5))

# Subplot 3 — list comprehension que crea una lista de arrays
# cada array contiene todos los ingresos de una ciudad
# boxplot necesita los datos separados así: [array_cdmx, array_mty, ...]
ticket_ciudad = [df[df["ciudad"] == ciudad]["ingreso"].values
                 for ciudad in df["ciudad"].unique()]

# guardamos el orden de ciudades para usarlo como etiquetas del eje X
ciudades_orden = df["ciudad"].unique()

# Subplot 4 — value_counts cuenta cuántas veces aparece cada método de pago
# el resultado es una Serie: {"Tarjeta": 226, "Efectivo": 117, ...}
metodos = df["metodo_pago"].value_counts()

# =============================================================================
# FIGURA PRINCIPAL
# =============================================================================

# subplots(2, 2) crea una cuadrícula de 2 filas × 2 columnas = 4 gráficas
# figsize controla el ancho y alto total de la figura en pulgadas
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# suptitle agrega un título general que abarca toda la figura
# y=1.01 lo sube un poco para que no choque con los subplots
fig.suptitle("Dashboard de Ventas 2024", fontsize=16, fontweight="bold", y=1.01)

# lista de nombres de meses para reemplazar los números 1-12 en el eje X
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
         "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

# =============================================================================
# SUBPLOT 1 — VENTAS POR MES (gráfica de línea)
# axes[0, 0] = fila 0, columna 0 (arriba izquierda)
# =============================================================================
ax1 = axes[0, 0]

# plot dibuja la línea — marker="o" agrega un punto en cada mes
ax1.plot(ventas_mes.index, ventas_mes.values,
         color="#4C72B0", marker="o", linewidth=2, markersize=5)

# fill_between rellena el área bajo la línea — alpha controla la transparencia
ax1.fill_between(ventas_mes.index, ventas_mes.values, alpha=0.1, color="#4C72B0")

# títulos y etiquetas de ejes
ax1.set_title("Ventas totales por mes")
ax1.set_xlabel("Mes")
ax1.set_ylabel("Ingreso ($)")

# set_xticks define dónde van las marcas del eje X (posiciones 1 al 12)
ax1.set_xticks(ventas_mes.index)

# set_xticklabels reemplaza los números por los nombres de los meses
ax1.set_xticklabels(meses, fontsize=9)

# FuncFormatter personaliza el formato del eje Y
# lambda recibe el valor y lo convierte a "$1,000,000" etc.
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))

# grid solo en el eje Y, con línea punteada y transparencia
ax1.grid(axis="y", linestyle="--", alpha=0.5)

# =============================================================================
# SUBPLOT 2 — TOP 5 CATEGORÍAS (barras horizontales)
# axes[0, 1] = fila 0, columna 1 (arriba derecha)
# =============================================================================
ax2 = axes[0, 1]

# barh dibuja barras horizontales — h de horizontal
# retorna el objeto bars que usamos después para agregar etiquetas
bars = ax2.barh(top_categorias.index, top_categorias.values, color="#55A868")

ax2.set_title("Top 5 categorías por ingreso")
ax2.set_xlabel("Ingreso total ($)")

# formateamos el eje X en millones — x/1e6 convierte a millones
ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x/1e6:.1f}M"))

# bar_label agrega etiquetas de texto al final de cada barra
# padding separa la etiqueta de la barra
ax2.bar_label(bars,
              labels=[f"${v/1e6:.1f}M" for v in top_categorias.values],
              padding=5, fontsize=9)

ax2.grid(axis="x", linestyle="--", alpha=0.5)

# =============================================================================
# SUBPLOT 3 — TICKET POR CIUDAD (boxplot)
# axes[1, 0] = fila 1, columna 0 (abajo izquierda)
# ==============================================================
