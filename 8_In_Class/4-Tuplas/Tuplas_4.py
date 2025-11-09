#Funcion para ingresar un pais y su poblacion en una lista llamada pais, almacenada en tuplas
def IngresarPaisPoblacion():
    pais = []
    for x in range(5):
        nombre = input("Ingrese el nombre del pais: ")
        cantidad = int(input("Ingrese cantidad de habitantes: "))
        pais.append((nombre, cantidad))
    return pais

#Funcion que imprime de manera ordenada el pais y la cantida de habitantes que este tiene
def imprimir(paises):
    print("Paises y su Poblacion: ")
    for x in range(len(paises)):
        print(paises[x][0], paises[x][1])

#Funcion que compara la primera tupla que esta en la posicion 0, con la segunda y el resto, con el objetivo de que si
#Alguna de las que sigue es mayor este reemplaze a la posicion 0 para que de este modo despues se pueda imprimir

def paismayorpoblacion(paises):
    posicion = 0
    for x in range(1, len(paises)):
        if (paises[x][1] > paises[posicion][1]):
            pos = x
    print("Pais con mayor cantidad de habitantes", paises[pos][0])

#Principal
#Llamada de las funciones
paises = IngresarPaisPoblacion()
imprimir(paises)
paismayorpoblacion(paises)