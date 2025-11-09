#Funcion que almacena nombre y suelo en tuplas en una lista llamada empleados
def carga():
    empleados = []
    for x in range(3):
        nombre = input("Ingrese nombre: ")
        sueldo = int(input("Ingrese sueldo: "))
        empleados.append((nombre, sueldo))
    return empleados

def imprimir(empleados):
    print("Listado de empleados (Nombre y sueldo): ")
    for nombre, sueldo in empleados:
        print(nombre, sueldo)

def mayor_sueldo(empleados):
    empleado_mayor_sueldo = empleados[0]
    for emp in empleados:
        if emp[1] > empleado_mayor_sueldo[1]:
            empleado_mayor_sueldo = emp
    print(f"Empleado con mayor sueldo: {empleado_mayor_sueldo[0]}, su sueldo es: {empleado_mayor_sueldo[1]}")

# PRINCIPAL
empleados = carga()
imprimir(empleados)
mayor_sueldo(empleados)