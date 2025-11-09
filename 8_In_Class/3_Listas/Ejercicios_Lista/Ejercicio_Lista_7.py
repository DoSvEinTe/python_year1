#Lista vacia
sueldos = []

#Ciclo for que agrega elementos a la lista normalmente
for x in range(5):
    valor = int(input("Ingrese su sueldo: "))
    sueldos.append(valor)

#Imprime la lista sin estar ordenado
print("Lista sin ordenar el mayor: ")
print(sueldos)

#Metodo "Bubble sort" para ordenar los numeros ingresados de menor a mayor
for k in range(4):
    for x in range(4):
        if sueldos[x] > sueldos[x + 1]:
            aux = sueldos[x]
            sueldos[x] = sueldos [x + 1]
            sueldos[x + 1] = aux

#Esto imprime la lista de menor a mayor
print(f"Lista ordenada: {sueldos}")