# Lista para almacenar los productos
lista = []

# Ciclo para ingresar 5 productos
for i in range(5):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el valor del producto: "))
    lista.append((nombre, precio))

# Imprimir los productos ingresados
for i in range(5):
    print(f"El nombre del producto es: {lista[i][0]}")
    print(f"El precio del producto es: {lista[i][1]}\n")

# Lista para almacenar productos con precio mayor a 15
lista_mayor_15 = []

# Revisar cada producto en la lista
for nombre, precio in lista:
    if precio <= 15 and precio >= 10:
        lista_mayor_15.append((nombre, precio))

# Imprimir los productos con precio mayor a 15
print("Los productos con un valor mayor a 15 son:")
for nombre, precio in lista_mayor_15:
    print(f"Nombre: {nombre}, Precio: {precio}")
