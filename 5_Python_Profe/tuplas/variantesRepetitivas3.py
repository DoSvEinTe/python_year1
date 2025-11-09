def cargar():
    empleados=[]
    for x in range(3):
        nombre=input('Ingrese Nombre:')
        sueldo=int(input('Ingrese Sueldo:'))
        empleados.append ((nombre,sueldo))
    return empleados

def imprimir(empleados):
    print('Listado de Empleados (Nombre y sueldo)')
    for nombre,sueldo in empleados:
        print(nombre,sueldo)

def mayotSueldo(empleados):
    empleado=empleados[0]
    for emp in empleados:
        if emp[1]>empleado[1]:
            empleado=emp
    print('Empleado con Mayor sueldo:',empleado[0],"su sueldo es:",empleado[1])

#principal
empleados=cargar()
imprimir(empleados)
mayotSueldo(empleados)