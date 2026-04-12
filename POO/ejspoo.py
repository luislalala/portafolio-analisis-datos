### ejercicio nivel basico 
# Objetivo: Modelar una clase simple con atributos y métodos.
# Contexto: Estás construyendo un sistema para una escuela pequeña.
# Tareas:
# Crea una clase Estudiante con atributos: nombre, edad, calificaciones (lista de números)
# Método promedio() que retorne el promedio de sus calificaciones
# Método estado() que retorne "Aprobado" si el promedio ≥ 6, sino "Reprobado"
# Método __str__ para imprimir la info del estudiante de forma legible
class Estudiante: #creamos la clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad  
        self.calificaciones = [] 
    def agregar_calificación(self, calificacion):
        if isinstance(calificacion, int): #estamos poniendo la condicion de que calificacion debe ser un dato de tipo entero 
            self.calificaciones.append(calificacion) #agregamos la calificacion a la lista vacia 
        else: return "escribe un velor numerico"
    def promedio(self):
        if not self.calificaciones:  #pregunta si algo es false o en este caso si la lista esta vacia 
            return 0
        return sum(self.calificaciones) / len(self.calificaciones) #se calcula el promedio 
    def estado(self):
        if self.promedio() >= 6: #evaluamos el promedio para saber si el estudiante paso o no 
            return "Estudiante Aprobado"
        else: return "Estudiante reprobado"
    def __str__(self):
        return f"Estudiante: {self.nombre} | Edad: {self.edad} | Promedio: {self.promedio()} | Estado: {self.estado()} "
    #str son los valores que queremos que se impriman 

name = input("introduce nombre del estudiante: ").lower().strip()
ed = int(input("introduce edad del estudiante: "))
est = Estudiante(name, ed)
while True: #es el bucle que nos permite insertar cuantas calificaciones nececitemos 
    clf = input("introduce calificación: ")
    if clf.lower().strip() == "promedio":
        print(est)
        break
    else:
        try:
            clf = int(clf)
            est.agregar_calificación(clf)
        except ValueError: print("Por favor introduce un valor valido")

### EJERCICIO NIVEL INTERMEDIO 
# Objetivo: Usar herencia y encapsulamiento.
# Contexto: Una tienda necesita controlar su inventario de productos.
# Tareas:
# Clase base Producto con: nombre, precio, _stock (privado)
# Métodos: agregar_stock(cantidad), vender(cantidad) (valida que haya suficiente stock), __str__
# Clase hija ProductoPerecible(Producto) que añada: fecha_vencimiento y método esta_vencido() comparando con la fecha actual (datetime)
# Clase hija ProductoElectronico(Producto) que añada: garantia_meses y método info_garantia()
# Crea una lista mixta de productos y filtra los perecederos vencidos

class Producto:
    def __init__(self, producto, precio, stock):
        self.producto = producto
        self.precio = precio
        self._stock = stock
    def agregar_stock(self, cantidad):
        if isinstance(cantidad, int):
            self._stock += cantidad #estamos sumando la cantidad a stock y le da ese valor a stock 
            return f"stock actual: {self._stock}"
        else: print("introduce un valor numerico")
    def vender(self, cantidad):
        if cantidad > self._stock:
            return "stock insuficiente"
        else:
            self._stock -= cantidad #le resta cantidad a stock y le da ese valor a stock
            return f"cantidad restante {self._stock}"
    def __str__(self):
        return f"Producto: {self.producto} | Precio: {self.precio} | Stock: {self._stock}"

from datetime import date
class ProductoPerecedero(Producto): #es una clase con la herencia de la clase producto 
    def __init__(self, producto, precio, stock, caducidad):
        super().__init__(producto, precio, stock)
        self.caducidad = caducidad
    def esta_vencido(self):
        fecha_del_dia = date.today() #da la fecha del dia 
        return fecha_del_dia > self.caducidad #compara la caducidad con la fecha de ese dia 
    def __str__(self):
        estado = "VENCIDO " if self.esta_vencido() else f"Vence: {self.caducidad}"
        return super().__str__() + f" | {estado}"
        
class ProductoElectronico(Producto):
    def __init__(self, producto, precio, stock, garantia):
        super().__init__(producto, precio, stock)
        self.garantia = garantia
    def info_garantia(self):
        fecha_del_dia = date.today()
        if fecha_del_dia > self.garantia:
            return f"la garantia de este producto vencio el dia {self.garantia}"
        else: return f"la garantia de este producto es valida"
    def __str__(self):
        return super().__str__() + f" | {self.info_garantia()}"

inventario = [ # es el inventario 
    ProductoPerecedero("Jamón", 55, 10, date(2025, 4, 1)),
    ProductoPerecedero("Queso", 80, 7, date(2026, 6, 15)),
    ProductoElectronico("Teléfono", 3000, 5, date(2027, 1, 1)),
    ProductoPerecedero("Leche", 25, 20, date(2025, 3, 1)),
    ProductoElectronico("Bocina", 2000, 3, date(2026, 8, 10)),
]
vencidos = [p for p in inventario 
            if isinstance(p, ProductoPerecedero) and p.esta_vencido()] #si p es un producto perecedero y evalua si p esta caducado 
print("=== Inventario completo ===")
for p in inventario:
    print(p)

print("\n=== Productos vencidos ===")
for p in vencidos:
    print(p)
