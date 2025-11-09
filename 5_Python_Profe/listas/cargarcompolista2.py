nombres=[]
sueldos=[]
totalsueldos=[]

for x in range(3):
    nombre=input('Nombre:')
    nombres.append(nombre)
    s1=int(input('Sueldo 1:'))
    s2=int(input('Sueldo 2:'))
    s3=int(input('Sueldo 3:'))
    sueldos.append([s1,s2,s3])
# recorrer la lista y sumar los 3 sueldos de cada empleado y agregarlos
for x in range(3):
    total=sueldos[x][0]+sueldos[x][1]+sueldos[x][2]
    totalsueldos.append(total)
# mostrar por pantalla el total de sueldos pagados de los 3 meses por empleado
for x in range(3):
    print(nombre[x],totalsueldos[x])
#obtener el empleado con mayor sueldo acumulado
posmayor=0
mayor=totalsueldos[0]
for x in range(1,3):
    if totalsueldos[x]>mayor:
        mayor=totalsueldos[x]
        posmayor=x

print("Empleado con mayores ingreses en los 3 meses:")
print(nombres[posmayor])
print("Con un ingreso total:",mayor)


