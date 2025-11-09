nombres=[]
notas=[]

for x in range(3):
    nombre=input('Ingresar Nombre:')
    nombres.append(nombre)
    n1=float(input('Ingrese Nota 1:'))
    n2=float(input('Ingrese Nota 2:'))
    notas.append([n1,n2])

for x in range(3):
    print(nombres[x],notas[x][0],notas[x][1])