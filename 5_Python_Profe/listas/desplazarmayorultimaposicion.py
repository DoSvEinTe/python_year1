# dejar el mayor al final de la lista
sueldos=[]
for x in range(5):
    valor=int(input('Ingrese sueldo:'))
    sueldos.append(valor)

print('Lista sin Ordenar el mayor')
print(sueldos)

for x in range(4):
    if sueldos[x]>sueldos[x+1]:
        aux=sueldos[x]
        sueldos[x]=sueldos[x+1]
        sueldos[x+1]=aux

print('Lista con el ultimo elemento mayor al final de la lista')
print(sueldos)
