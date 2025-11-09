def carga():
    lista = []
    for x in range(5):
        numero = int(input("Ingrese valor: "))
        lista.append(numero)
    return lista

def imprimir(lista):
    print("Lista completa: ")
    for elemento in lista:
        print(elemento)

def mayor(lista):
    mayor = lista[0]
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
    print(f"El elemento mayor de la lista es: {mayor}")

def suma_elemento(lista):
    suma = 0
    for elemento in lista:
        suma = suma + elemento
    print(f"La suma de todos los elementos es: {suma}")

# PRINCIPAL
lista = carga()
imprimir(lista)
mayor(lista)
suma_elemento(lista)