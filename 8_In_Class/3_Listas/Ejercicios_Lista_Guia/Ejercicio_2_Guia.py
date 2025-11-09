listas = []
lista_aux = []

for i in range(1, 6):
    lista = int(input("Ingrese un valor mayor o igual a 7: "))
    listas.append(lista)

    if lista >= 7:
        lista_aux.append(lista)

print("########################################\n")
print(f"La lista completa es: {listas}")
print(f"Los valores mayor a 7 en la lista son: {lista_aux}")
print("\n########################################")
