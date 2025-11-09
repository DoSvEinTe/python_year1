lista=[2,4,50,7,9]
print(lista)

for x in range(len(lista)):
    if lista[x]<10:
        lista[x]=0

print(lista)
print('usando otro tipo de for')
for elemento in lista:
    print(elemento)
