def contador_vocales(variable):

    #Acumulador de vocales

    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0

    #Contador de vocales

    for vocal in variable:
        if vocal == "a" or vocal == "A":
            contador_a += 1
        elif vocal == "e" or vocal == "E":
            contador_e += 1
        elif vocal == "i" or vocal == "I":
            contador_i += 1
        elif vocal == "o" or vocal == "O":
            contador_o += 1
        elif vocal == "u" or vocal == "U":
            contador_u += 1
    print("#################################################################################")
    print("")
    print("Hay un total de {} vocal (a) en tu codena de texto ingresada".format(contador_a))
    print("Hay un total de {} vocal (e) en tu codena de texto ingresada".format(contador_e))
    print("Hay un total de {} vocal (i) en tu codena de texto ingresada".format(contador_i))
    print("Hay un total de {} vocal (o) en tu codena de texto ingresada".format(contador_o))
    print("Hay un total de {} vocal (u) en tu codena de texto ingresada".format(contador_u))
    print("")
    print("#################################################################################")

#Salida de datos

variable = str(input("Ingrese una cadena de texto: "))

contador_vocales(variable)