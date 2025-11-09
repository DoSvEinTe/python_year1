#Creacion de una lista vacia
lista= []

#Bucle For en el cual se ingresa un valor preguntado al usuario y se acumula en la lista con el modulo append
for x in range(5):
    valor = int(input("Ingrese un valor: "))
    lista.append(valor)

#Creacion de variables para encontrar el mayor de la lista y la posicion en la que este se encuentra
mayor = lista[0]
posicion = 0

#Se crea un bucle for para encontrar el mayor de la lista, el ciclo va del 1 al 4 ya que se asume que el mayor es el que esta en la poscicion 0
#Y se confirma con el if, si el numero de la posicion numero 0 llegara a ser menor que el de la lista "x" entonces dentro del bucle se reemplazaria
#Al igual que la posicion

for x in range(1, 5): #Bucle del 1 al 4
    if lista[x] > mayor: #Confirmacion si desde la posicion 1 al 4 algun numero es mayor a la posicion numero 0
        mayor = lista[x] #Se reemplaza el valor si esque llegara ser mayor
        posicion = x #Se reemplaza la posicion si esque llegara a ser distinta

#Salida de datos
print(f"Lista completa: {lista}")
print(f"El mayor de la Lista es: {mayor}")
print(f"La posicion del mayor en la lista es: {posicion}")