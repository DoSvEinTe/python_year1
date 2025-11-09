lista=[]
valor=int(input("Ingrese un valor (0 para terminar): "))
#El usuario ingresa un valor, este ciclo se repetira mientras el valor ingresado sea diferente a 0, si el valor es 0 el ciclo parara automaticamente
while valor!=0:
    lista.append(valor)
    valor=int(input("Ingrese un valor (0 para terminar): "))
#Imprime la cantidad total de elementos que contiene la lista
print(f"Tamaño de la lista: {len(lista)}")
#Imprime todos los elementos de la lista
print(f"Lista: {lista}")