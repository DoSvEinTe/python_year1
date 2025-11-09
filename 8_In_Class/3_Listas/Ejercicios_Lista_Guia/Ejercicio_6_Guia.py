sueldos = []
sueldos_mañana = []
sueldos_tarde = []

for i in range(8):
    print("\n1 - Trabajador de turno de mañana")
    print("0 - Trabajador de turno de noche\n")
    confirmacion = int(input("Ingrese su turno: "))

    if confirmacion == 1:
        sueldo = float(input("Ingrese su sueldo: "))
        sueldos_mañana.append(sueldo)
    
    if confirmacion == 0:
        sueldo = float(input("Ingrese su sueldo: "))
        sueldos_tarde.append(sueldo)

print("___________________LISTA 1___________________")
print("_________________TURNO MAÑANA________________")
for i in range(4):
    print(sueldos_mañana[i])
print("___________________LISTA 2___________________")
print("__________________TURNO TARDE________________")
for i in range(4):
    print(sueldos_mañana[i])