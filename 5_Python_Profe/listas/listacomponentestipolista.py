lista=[[1,2,3],[4,5,6], [7,8,9]]
   #     0        1         2 
# IMPRIMIR LA LISTA COMPLETA
print('IMPRIMIR LA LISTA COMPLETA')
print(lista)
print('------------------------------------')
print('IMPRIMIR EL PRIMER COMPONENTE')
print(lista[0])
print('------------------------------------')
print('IMPRIMIR EL PRIMER COMPONENTE CONTENIDO DE LA LISTA')
print(lista[1])
print(lista[2])
print('IMPRIMIR EL PRIMER COMPONENTE CONTENIDO DE LA LISTA')
print(lista[0][0])
print(lista[1][0])
print(lista[2][2])
print('------------------------------------')
print('IMPRIMIR CON UN FOR LS LISTA CONTENIDOS EN EL PRIMER COMPONENTE')
for x in range(len(lista[0])):
    print(lista[2][x])
print('------------------------------------')

print('IMPRIMIR CADA ELEMENTO ENTERO DE CADA LISTA CONTENIDA EN LA LISTA')
for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])
