#funciones llamada a la función con argumentos nombrados

def calcular_sueldo(nombre,costohora,cantidadhoras):
    sueldo=costohora*cantidadhoras
    print(nombre,"trabajo",cantidadhoras," y cobra un sueldo de",sueldo)

#bloque principal
calcular_sueldo("Juan",10,120)
calcular_sueldo(costohora=12,cantidadhoras=40,nombre="Vanesa")
calcular_sueldo(cantidadhoras=90,nombre="Pedro",costohora=7)
