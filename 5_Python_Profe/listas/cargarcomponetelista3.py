padres=[]
hijos=[]

for k in range(3):
    padre=input('Nombre Padre:')
    madre=input('Nombre Madre:')
    padres.append([padre,madre])
    cant=int(input('Cantidad de hijos en la familia:'))
    hijos.append([])
    for x in range(cant):
        nombre=input('Nombre Hijo:')
        hijos[k].append(nombre)

print('LISTADO DEL PADRE,MADRE y SUS HIJOS:')
for k in range(3):
    print('Padre:',padres[k][0])
    print('Madre:',padres[k][1])
    for x in range(len(hijos[k])):
        print('Hijo:',hijos[k][x])

print('LISTADO DEL PADRE y CANTIDAD DE HIJOS QUE TIENE:')
for x in range(3):
    print('Padre:;',padres[x][0])
    print('cantidad de hijos:',len(hijos[x]))