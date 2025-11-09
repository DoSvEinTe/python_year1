# Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios.
# Definir las siguientes funciones:
# 1) Cargar los nombres de articulos y sus precios.
# 2) Imprimir los nombres y precios.
# 3) Imprimir el nombre de artículo con un precio mayor
# 4) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado.

def carga_datos():
    #Listas vacias

    lista_nombres = []
    lista_precios = []

    #Entrada y almacenamiento de datos en la lista
    for i in range(5):
        nombre = input("Ingrese el nombre de su articulo: ")
        lista_nombres.append(nombre)
        precio = float(input("Ingrese el valor de su articulo: "))
        lista_precios.append(precio)

    return lista_nombres, lista_precios

def impresion(lista_nombres, lista_precios):
    for i in range(5):
        print(f"El nombre del producto es: {lista_nombres[i]}, y su precio es: {lista_precios[i]}")

def dato_mayor(lista_nombres, lista_precios):
    
    max_precio = lista_precios[0]
    posicion = 0

    for i in range(1, len(lista_precios)):
        if lista_precios[i] > max_precio:
            max_precio = lista_precios[i]
            posicion = i

    print(f"{lista_nombres[posicion]} es el elemento que más vale en la lista y tiene un precio de {max_precio}")

def comparacion(lista_nombres, lista_precios):
    importe = float(input("Ingrese el valor que desea comparar: "))

    lista_posiciones = []

    for i in range(len(lista_precios)):
        if lista_precios[i] < importe:
            lista_posiciones.append(i)
    
    for i in lista_posiciones:
        print(f"{lista_nombres[i]} es menor al importe ingresado y tiene un valor de {lista_precios[i]}")

            
#Bloque principal

lista_nombres, lista_precios = carga_datos()
impresion(lista_nombres, lista_precios)
dato_mayor(lista_nombres, lista_precios)
comparacion(lista_nombres, lista_precios)