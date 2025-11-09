alturas = []
alturas_alta = []
alturas_baja = []
acum = 0

for i in range(5):
    altura = float(input("Ingrese su altura: "))
    alturas.append(altura)
    acum += altura

promedio = acum / 5

for i in range(5):
    if alturas[i] >= promedio:
        alturas_alta.append(alturas[i])
    else:
        alturas_baja.append(alturas[i])

print("_______________________________________________________________")
print(f"\nLa lista de alturas ingresadas es: {alturas}")
print(f"El promedio de altura de las 5 personas es {promedio}")
print(f"Las alturas que estan arriba del promedio son: {alturas_alta}")
print(f"Las alturas que estan debajo del promedio son: {alturas_baja}\n")
print("_______________________________________________________________")
