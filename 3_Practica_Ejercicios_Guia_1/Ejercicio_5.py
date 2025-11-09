# Crear una lista de enteros por asignación. Definir una función que reciba una lista de enteros y 
# un segundo parámetro de tipo entero. Dentro de la función mostrar cada elemento de la lista multiplicado por el 
# valor entero enviado.
#
# lista=[3, 7, 8, 10, 2]
# multiplicar(lista,3)

def list_enteros():
    
    lista = []
    
    while True:
        num1 = input("Ingrese un valor entero para ser agregado a la lista: ")
        lista.append(num1)

        print("SI = 1")
        print("NO = 0")
        confirmacion = int(input("¿Quiere continuar?: "))

        if confirmacion == 0:
            break
    
    return lista

numero = int(input("Ingrese el valor del numero al cual quiere multiplicar la lista: "))

def multiplicar_list(lista, numero):
    for i in lista:
        print(f"{i} x {numero} = {i * numero}")

lista = list_enteros()
print(f"La lista de numero ingresados es: {lista}")
print(f"La multiplicacion de {numero} por los numeros de la lista es: ")
multiplicar_list(lista, numero)
