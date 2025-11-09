sueldos = []
promedio = 0

for i in range(5):
    sueldo = float(input("Ingrese su sueldo: "))
    sueldos.append(sueldo)

    promedio += sueldo

resultado_prom = promedio / 5

print("_________________________________________________________")
print(f"\nLos sueldos ingresados son: {sueldos}")
print(f"Y el promedio de todos los sueldos son: {resultado_prom}\n")
print("_________________________________________________________")