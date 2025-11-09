padres = []
hijos = []

for k in range(3):
    padre = input("Nombre del padre: ")
    madre = input("Nombre de la madre: ")
    padres.append([padre, madre])
    cantidad = int(input("Cantidad de hijos en la familia: "))
    hijos.append([])

    for x in range(cantidad):
        nombre = input("Nombre hijo(a): ")
        hijos[k].append(nombre)

print("LISTADO DEL PADRE, LA MADRE Y SUS HIJOS")
for k in range(3):
    print(f"Padre: {padres[k][0]}")
    print(f"Madre: {padres[k][1]}")

    for x in range(len(hijos[k])):
        print(f"Hijo: {hijos[k][x]}")

print("LISTADO DEL PADRE Y CANTIDAD DE HIJOS QUE TIENE")
for x in range(3):
    print(f"Padre:; {padres[k][0]}")
    print("Cantidad de hijos:", len(hijos[x]))