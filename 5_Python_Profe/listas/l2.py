lista=[20,30,7,3,2]
x=0
acum=0

while x<len(lista):
    print('Lista:',lista[x])
    acum=acum+lista[x]
    print('Acumulador',acum)
    #x=x+1
    x+=1

print('Contenidos de la lista',lista)
print("La suma de sus elementos es:\t",acum)
