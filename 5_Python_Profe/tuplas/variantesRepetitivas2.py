def cargar():
    lista=[]
    for x in range(5):
        num=int(input('Ingrese valor:'))
        lista.append(num)
    return lista

def imprimir(lista):
    print('List completa')
    for elemento in lista:
        print(elemento)

def mayor(lista):
    may=lista[0]
    for elemento in lista:
        if elemento>may:
            may=elemento
    print('El elemento mayor de la lista es:',may)

def sumaElementos(lista):
    suma=0
    for elemento in lista:
        suma=suma+elemento
    print('La suma de todos sus elementos es:',suma)
#principal
lista=cargar()
imprimir(lista)
mayor(lista)
sumaElementos(lista)