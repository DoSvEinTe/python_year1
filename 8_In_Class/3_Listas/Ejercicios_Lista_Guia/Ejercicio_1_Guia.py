listas = []

acum = 0

for i in range(1, 9):
    lista = int(input("Ingrese un valor entero: "))
    listas.append(lista)

    if lista > 100:
        acum = acum + 1

print("#########################################")
print("")
print(f"La lista acumulada es: {listas}")
print(f"Y la cantidad de numeros almacenados mayores a 100 son: {acum}")
print("")
print("#########################################")

