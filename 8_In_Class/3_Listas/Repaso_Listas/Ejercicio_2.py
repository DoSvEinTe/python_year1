nombres = []
sueldos = []
total_sueldos = []

for x in range(3):
    nombre = input("Nombre: ")
    nombres.append(nombre)
    s1 = int(input("Sueldo 1: "))
    s2 = int(input("Sueldo 2: "))
    s3 = int(input("Sueldo 3: "))
    sueldos.append([s1, s2 , s3])

# RECORRER LA LISTA Y SUMAR LOS 3 SUELDOS DE CADA EMPLEADO Y AGREGALOS.
for x in range(3):
    total = sueldos[x][0] + sueldos[x][1] + sueldos[x][2]
    total_sueldos.append(total)

# MOSTRAR POR PANTALLA EL TOTAL DE SUELDOS PAGADOS DE LOS 3 MESES POR EMPLEADO.
for x in range(3):
    print(nombre[x], total_sueldos[x])

# OBTENER EL EMPLEADO CON MAYOR SUELDO ACUMULADO.
pos_mayor = 0
mayor = total_sueldos[0]
for x in range(1, 3):
    if total_sueldos[x] > mayor:
        mayor = total_sueldos[x]
        pos_mayor = x

print("EMPLEADO CON MAYORES INGRESES EN LOS 3 MESES")
print(nombres[pos_mayor])
print(f"CON UN INGRESO TOTAL: {mayor}")