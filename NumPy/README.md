# 🔷 NumPy — Operaciones Matriciales y Estadística

Ejercicios que demuestran el uso de NumPy para análisis estadístico,
operaciones matriciales y simulación, evitando loops de Python
en favor de operaciones vectorizadas.

---

## Ejercicio 1 — Análisis de ventas diarias (Nivel básico)

### ¿Qué problema resuelve?
Analiza las ventas diarias de una tienda durante 30 días,
calculando estadísticas descriptivas e identificando los días
de mayor rendimiento.

### Conceptos demostrados
- Generación de arrays aleatorios reproducibles (`seed`)
- Estadística descriptiva: media, mediana, desviación estándar
- Ordenamiento por índices con `np.argsort`
- Máscaras booleanas para filtrado vectorizado
- Cálculo de porcentajes sobre arrays booleanos

### Resultados obtenidos
```
Media de ventas:        ~567
Mediana:                ~556
Desviación estándar:    ~261
Top 5 días de ventas:   índices [x, x, x, x, x]
Días sobre la media:    ~53%
```

---

## Ejercicio 2 — Correlación de Pearson manual (Nivel intermedio)

### ¿Qué problema resuelve?
Calcula la matriz de correlación de Pearson entre 4 variables
sin usar `np.corrcoef`, implementando la fórmula matemática
paso a paso con operaciones matriciales.

### Conceptos demostrados
- Generación de matrices aleatorias con distribución normal
- Centrado de datos por columnas (`axis=0`)
- Producto matricial con `np.dot`
- Broadcasting con `np.outer`
- Verificación de resultados con `np.allclose`
- Identificación de máximos/mínimos ignorando diagonal (`np.nan`)

### Proceso matemático implementado

```
1. Centrar datos:     X_c = X - mean(X, axis=0)
2. Covarianza:        C = Xc.T · Xc / (n-1)        → matriz 4x4
3. Desv. estándar:    σ = sqrt(diag(C))
4. Correlación:       R = C / outer(σ, σ)
```

### Verificación
```python
np.allclose(correlacion_manual, np.corrcoef(matriz.T))
# True — el cálculo manual coincide con NumPy
```

### Resultado
```
Par con mayor correlación: variables (i, j) → r = x.xxxx
Par con menor correlación: variables (i, j) → r = x.xxxx
```
