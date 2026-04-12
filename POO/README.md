# 🔷 POO — Programación Orientada a Objetos

Ejercicios que modelan sistemas reales aplicando los principios
fundamentales de la programación orientada a objetos en Python.

---

## Ejercicio 1 — Sistema escolar (Nivel básico)

### ¿Qué problema resuelve?
Modela el registro de calificaciones de estudiantes en una escuela,
calculando promedios y determinando automáticamente si un estudiante
aprobó o reprobó.

### Conceptos demostrados
- Clase con atributos de instancia
- Métodos que retornan valores calculados
- Método `__str__` para representación legible
- Validación de tipos con `isinstance()`
- Manejo de errores con `try / except`

### Estructura de la clase
```
Estudiante
├── __init__(nombre, edad)
├── agregar_calificacion(calificacion)
├── promedio()
├── estado()
└── __str__()
```

### Ejemplo de uso
```python
est = Estudiante("Ana", 20)
est.agregar_calificacion(8)
est.agregar_calificacion(7)
est.agregar_calificacion(9)
print(est)
# Estudiante: ana | Edad: 20 | Promedio: 8.0 | Estado: Estudiante Aprobado
```

---

## Ejercicio 2 — Control de inventario (Nivel intermedio)

### ¿Qué problema resuelve?
Sistema de inventario para una tienda que maneja dos tipos de productos:
perecederos (con fecha de caducidad) y electrónicos (con garantía).
Detecta automáticamente qué productos están vencidos.

### Conceptos demostrados
- Herencia: clases hijas que extienden una clase base
- Encapsulamiento: atributo privado `_stock`
- Polimorfismo: `__str__` personalizado en cada clase
- Uso de `datetime` para comparación de fechas
- Filtrado con `isinstance()` sobre listas mixtas

### Estructura de clases
```
Producto (clase base)
├── __init__(producto, precio, stock)
├── agregar_stock(cantidad)
├── vender(cantidad)
└── __str__()

ProductoPerecedero(Producto)
├── __init__(..., caducidad)
├── esta_vencido()          → bool
└── __str__()               → hereda y extiende

ProductoElectronico(Producto)
├── __init__(..., garantia)
├── info_garantia()         → str
└── __str__()               → hereda y extiende
```

### Resultado al ejecutar
```
=== Inventario completo ===
Producto: Jamón   | Precio: 55  | Stock: 10 | VENCIDO ⚠️
Producto: Queso   | Precio: 80  | Stock: 7  | Vence: 2026-06-15
Producto: Teléfono| Precio: 3000| Stock: 5  | la garantia es valida
Producto: Leche   | Precio: 25  | Stock: 20 | VENCIDO ⚠️
Producto: Bocina  | Precio: 2000| Stock: 3  | la garantia es valida

=== Productos vencidos ===
Producto: Jamón | Precio: 55 | Stock: 10 | VENCIDO ⚠️
Producto: Leche | Precio: 25 | Stock: 20 | VENCIDO ⚠️
```
