lista=[]

for x in range(5):
    valor=int(input('Ingrese un valor:'))
    lista.append(valor)

mayor=lista[0]
posicion=0
for x in range(1,5):
    if lista[x]>mayor:
        mayor=lista[x]
        posicion=x

print('Lista completa',lista)
print('El mayor de la lista es:',mayor)
print('La posicion del mayor en la lista es:',posicion)
