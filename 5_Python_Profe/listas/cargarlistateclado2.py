lista=[]
valor=int(input('Ingrese valor (0 para terminar):'))

while valor!=0:
    lista.append(valor)
    valor=int(input('Ingrese valor (0 para terminar):'))

print('Tamaño de la lista',len(lista))
print('Lista:',lista)