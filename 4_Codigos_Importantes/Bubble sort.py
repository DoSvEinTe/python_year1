"""
Ordenamiento burbuja o "Bubble sort", es un metodo que se utiliza para ordenar valores aleatorios,
esto se hace a traves de un ciclo for anidado, que nos va ordenar los valores segun lo requeramos,

Este metodo basicamente consiste en comparar el valor actual con el siguiente, y si el siguiente es mayor
(o menor), se va ir reemplazando asta lograr conseguir una lista que este completamente ordenada

Es importante recalcar que si hay 5 elementos por ejemplo hay que hacer el bucle 4 veces, ya que el penultimo valor se compara
con el ultimo valor, por ende el colocar 5 compararia el ultimo valor con nada
"""

sueldos = [150, 3, 40, 30, 21,]

for k in range(4):
    for x in range(4):
        if sueldos[x] > sueldos[x + 1]:
            aux = sueldos[x]
            sueldos[x] = sueldos [x + 1]
            sueldos[x + 1] = aux

print("__________________________")
print("\nEJEMPLO 1")
print("De menor a mayor\n")
print(sueldos)

sueldos = [150, 3, 40, 30, 21,]

for k in range(4):
    for x in range(4):
        if sueldos[x] < sueldos[x + 1]:
            aux = sueldos[x]
            sueldos[x] = sueldos [x + 1]
            sueldos[x + 1] = aux
print("__________________________")
print("\nEJEMPLO 2")
print("De mayor a menor\n")
print(sueldos)
print("")
print("__________________________")