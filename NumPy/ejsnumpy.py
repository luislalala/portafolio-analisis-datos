### EJERCICIO NIVEL BASICO 
# Objetivo: Operaciones fundamentales con arrays.
# Contexto: Tienes las ventas diarias de una tienda durante 30 días.
# Tareas:
# Genera un array con np.random.randint(100, 1000, size=30) (seed=42)
# Calcula: media, mediana, desviación estándar, mínimo y máximo
# Encuentra los índices de los 5 días con más ventas (np.argsort)
# Crea una máscara booleana para los días donde las ventas superaron la media
# Calcula qué porcentaje de días superaron la media
import numpy as np
np.random.seed(42)
array = np.random.randint(100, 1000, size=30) #crea una lista de 30 numeros aleatorios en un rango de 100 a 1000
media = np.mean(array) #calculamos la media de la lista 
mediana = np.median(array) #se calcula la mediana de la lista que seria el promedio del elemento 14 y 15
desviación = np.std(array) #calcula la desviacion estandar de la lista 
minimo = array.min() #el mas pequeño de la lista
maximo = array.max() #el mas grande de la lista 
ventas = np.argsort(array)[::-1] # argsort ordena los indices de menor a mayor, ::-1 es para que los acomode de mayor a menor 
mejores_ventas = ventas[:5] #es la cantidad de indices que queremos visualizar de argsort 
mascara = array > media #esta condicion nos entrega un boolean true or false 
porcentaje = mascara.mean() * 100 #calcula el porcentaje de todos los elemntos de array que revasaron la media 

### ejercicio nivel intermedio 
# Objetivo: Operaciones matriciales y broadcasting.
# Contexto: Tienes datos de 4 variables para 50 observaciones.
# Tareas:
# Genera una matriz (50, 4) con np.random.randn (seed=7)
# Sin usar np.corrcoef, calcula la correlación de Pearson manualmente entre todas las pares de columnas
# Construye la matriz de correlación (4x4) resultante
# Compara tu resultado con np.corrcoef para verificar
# Identifica el par de variables con mayor y menor correlación
np.random.seed(7) #es una semilla para que los numeros aleatorios siempre sean los mismos 
matriz =np.random.randn(50, 4) #se crea una matriz de 50x4 
datos_centrados = matriz - matriz.mean(axis=0 , keepdims=True) #a cada elemento de una columna estamos restando el promedio de esa columna
#usamos axis=0 para decir que estamos calculando el promedio de las filas 
# np.dot(datos_centrados.T, datos_centrados) multiplica (4x50) · (50x4) = matriz 4x4
# cada celda [i,j] contiene la suma de productos (col_i - media_i)(col_j - media_j)
# dividir entre n-1 convierte esa suma en covarianza muestral
covarianza = np.dot(datos_centrados.T, datos_centrados) / (len(matriz) - 1)
std = np.sqrt(np.diag(covarianza)) #los datos de la diagonal se convierten en la desviacion estandar 
correlacion_manual = covarianza / np.outer(std, std) #covariancia/producto de std
correlacion = np.corrcoef(matriz) 
if np.allclose(correlacion_manual, correlacion):
    print("la correlacion manual es correcta")
m_limpia = correlacion - np.eye(correlacion.shape[0]) #.shape dice la cantidad de columnas, filas y paredes al poner 0 esta contnado
#la cantidad de columnas, np.eye crea una matriz identidad, del tamayo cantidad de columna x cantidad de columnas
#al restar la matriz identidad a la matriz de correlacion queda una matriz de diagonal 0 
max_val = np.max(m_limpia)
idx_max = np.unravel_index(np.argmax(m_limpia), m_limpia.shape)
min_val = np.min(m_limpia)
idx_min = np.unravel_index(np.argmin(m_limpia), m_limpia.shape)
#np.arg te da numero del valor que pediste
#unravel de la coordenada del dato 
