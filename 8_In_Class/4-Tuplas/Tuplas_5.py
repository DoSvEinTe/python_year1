#Lista principal
lista = [2, 4, 50, 7, 9]
print(lista)

#Lista actualizada
for x in range(len(lista)):
    if lista[x] < 10: #Si la posicion actual es menor a 10 entonces
        lista[x] = 0 #Se convierte en 0, si no, sigue en la lista en este caso el unico mayor a 10 en la lista es 50
        #Por ende la lista que nos devuelve es [0, 0, 50, 0, 0]
print(lista)

print("Usando otro tipo de for")
for elemento in lista:
    print(elemento)


