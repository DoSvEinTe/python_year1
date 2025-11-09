# Confeccionar un programa que permita:
# 1) Cargar una lista de 10 elementos enteros.
# 2) Generar dos listas a partir de la primera. En una guardar los valores positivos y en otra los negativos.
# 3) Imprimir las dos listas generadas.

def cargar_elementos():

    lista_positiva = []
    lista_negativa = []

    for i in range(10):

        num1 = int(input("Ingrese un valor entero: "))

        if num1 < 0:
            lista_negativa.append(num1)
        else:
            lista_positiva.append(num1)
    
    print(f"Lista positiva: {lista_positiva}")
    print(f"Lista negativa: {lista_negativa}")

cargar_elementos()
