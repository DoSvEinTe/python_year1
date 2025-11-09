#Lista que coloca el numero mayor al final de la lista

#Se crea una lista vacia

sueldos = []

#Se ingresan 5 sueldos a traves de un ciclo for y se insertan en la lista "sueldos"

for x in range(5):
    valor = int(input("Ingrese su sueldo: "))
    sueldos.append(valor)

#Se imprime la lista normalmente, sin ordenar

print("Lista sin ordenar el mayor")
print(sueldos)

#Ciclo que intercambia valores si el valor actual es mayor al valor siguiente,
#valor actual sueldos[x]
#valor siguiente sueldos [x + 1]
#Si el actual es mayor al valor siguiente se intercambian los valores a traves de la variable "aux"
#y por ende el que tiene el vaor mayor quedaria al final de la lista

for x in range(4):
    if sueldos[x] > sueldos[x + 1]:
        aux = sueldos[x]
        sueldos[x] = sueldos [x + 1]
        sueldos[x + 1] = aux

#Finalmente se imprimiria la lista con el valor mayor al final de esta

print("Lista con el ultimo elemento mayor al final de la Lista")
print(sueldos)