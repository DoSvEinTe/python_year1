# En una empresa se almacenaron los sueldos de 10 personas.
# Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
# 1) Carga de los sueldos en una lista.
# 2) Impresión de todos los sueldos.
# 3) Cuántos tienen un sueldo superior a $4000.
# 4) Retornar el promedio de los sueldos.
# 5) Mostrar todos los sueldos que están por debajo del promedio.


def carga_datos():
    lista_sueldos = []
    for i in range(10):
        sueldo = int(input("Ingrese su sueldo: "))
        lista_sueldos.append(sueldo)
    return lista_sueldos

def impresion(sueldos):
    print("LISTA DE SUELDOS")
    for i in sueldos:
        print(f"-{i}")

def superior(sueldos):
    contador = 0
    for i in sueldos:
        if i > 4000:
            contador += 1
    print(f"Hay un total de {contador} personas que tienen un sueldo mayor a 4000")

def promedio(sueldos):
    acumulador = 0
    for i in sueldos:
        acumulador += i
    promedio = acumulador / len(sueldos)
    print(f"El promedio de la lista de sueldos es {promedio}")
    return promedio

def debajo_prom(promedio, sueldos):
    lista_infe = []
    for i in sueldos:
        if i < promedio:
            lista_infe.append(i)
    print("LISTA DE SUELDOS INFERIOR AL PROMEDIO")
    for i in lista_infe:
        print(f"-{i}")

sueldos = carga_datos()
promedio_sueldos = promedio(sueldos)
impresion(sueldos)
print("")
superior(sueldos)
print("")
debajo_prom(promedio_sueldos, sueldos)