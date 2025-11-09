nombres = []
caracteres_5 = []

for i in range(1, 6):
    nombre = input("Ingrese su nombre: ")
    nombres.append(nombre)

    if len(nombre) >= 5:
        caracteres_5.append(nombre)

print("\n___________________________________________________________________________")
print(f"\nLa lista completa de nombres es {nombres}")
print(f"Y la lista de nombres que tienen 5 o mas caracteres son {caracteres_5}\n")
print("___________________________________________________________________________\n")