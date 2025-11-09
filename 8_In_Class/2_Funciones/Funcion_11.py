def calcular(cadena):
    return len(cadena)#len cuenta la cantidad de caracteres que tiene una variable

#bloque principal

nombre1 = input("Ingrese primer nombre: ")
nombre2 = input("Ingrese segundo nombre: ")

largo1 = calcular(nombre1)
largo2 = calcular(nombre2)

if largo1 == largo2:
    print("Los nombres:",nombre1,nombre2,"tienen la misma cantidad de caracteres")
elif largo1 > largo2:
    print(nombre1,"\tes mas largo")
else:
    print(nombre2, "\tes mas Largo")