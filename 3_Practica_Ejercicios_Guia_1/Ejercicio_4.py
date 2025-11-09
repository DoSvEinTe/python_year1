# Crear un diccionario en Python para almacenar los datos de empleados de una empresa. La clave será su número de 
# legajo y en su valor almacenar una 
# lista con el nombre, profesión y sueldo.
# Desarrollar las siguientes funciones:
# 1) Carga de datos de empleados.


def carga_datos():
    empleados = {}

    while True:
        # Clave
        legajo = int(input("Ingrese su número de legajo: "))

        nombre = input("Ingrese su nombre: ")
        profesion = input("Ingrese su profesión: ")
        sueldo = float(input("Ingrese su sueldo: "))

        empleados[legajo] = [nombre, profesion, sueldo]

        print("¿Desea continuar agregando empleados?")
        print("NO = 0")
        print("SI = 1")

        confirmacion = input("Ingrese su opción: ")
        while confirmacion not in ('0', '1'):
            confirmacion = input("Opción inválida. Ingrese 0 para NO o 1 para SI: ")

        if confirmacion == '0':
            break

    return empleados

# 2) Permitir modificar el sueldo de un empleado. Ingresamos su número de legajo para buscarlo.

def modificar_sueldo(empleados):
    busqueda = int(input("Ingrese el legajo para buscar al empleado: "))

    if busqueda in empleados:
        nuevo_sueldo = float(input("Ingrese el nuevo sueldo del empleado: "))
        empleados[busqueda][2] = nuevo_sueldo
        print(f"Sueldo actualizado para el legajo {busqueda}.")
    else:
        print("El legajo ingresado no existe en el registro.")

    return empleados


# 3) Mostrar todos los datos de empleados que tienen una profesión de "analista de sistemas"

def analista_sistemas(empleados):
    lista_acumulativa = []

    for legajo, datos in empleados.items():
        if datos[1].lower() == "analista de sistemas":
            lista_acumulativa.append((legajo, datos))

    return lista_acumulativa

# Bloque principal
empleados = carga_datos()

print("Empleados ingresados:")
print(empleados)

print("\nModificación de sueldo:")
empleados = modificar_sueldo(empleados)

print("\nEmpleados con profesión 'analista de sistemas':")
analistas = analista_sistemas(empleados)
for legajo, datos in analistas:
    print(f"Legajo: {legajo}, Nombre: {datos[0]}, Profesión: {datos[1]}, Sueldo: {datos[2]}")
