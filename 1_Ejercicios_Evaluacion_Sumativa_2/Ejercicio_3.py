
def safe_contraseña():
    #Saber si la contraseña esta en mayuscula

    def caracter_mayusculas(contraseña):
        contador1 = 0
        for caracter in contraseña:
            if caracter.isupper():
                contador1 += 1
        return contador1
    
    #Saber si la contraseña esta en minuscula

    def caracter_minusculas(contraseña):
        contador2 = 0
        for caracter in contraseña:
            if caracter.islower:
                contador2 += 1
        return contador2
    
    #Saber si la contraseña tiene un numero

    def caracter_numero(contraseña):
        contador3 = 0
        for caracter in contraseña:
            if caracter.isdigit():
                contador3 += 1
        return contador3
    
    i = 0
    while i != 1:

        print("")
        print("Debe ingresar una contraseña segura, para ello considere lo siguiente")
        print("")
        print("- Debe tener al menos 8 caracteres")
        print("- Debe tener al menos 1 mayuscula")
        print("- Debe tener al menos 1 minuscula")
        print("- Debe tener al menos 1 numero")

        contraseña = input("Ingrese una contraseña segura: ")

        print("")

        longitud = len(contraseña)

        if longitud < 8:
            print("La contraseña debe tener al menos 8 caracteres")
        elif caracter_mayusculas(contraseña) == 0:
            print("La contraseña debe tener al menos 1 mayuscula")
        elif caracter_minusculas(contraseña) == 0:
            print("La contraseña debe tener al menos 1 minuscula")
        elif caracter_numero(contraseña) == 0:
            print("La contraseña debe tener al menos 1 numero")
        else:
            print("La contraseña es segura")
        
        #Romper el ciclo

            i = 1
        
safe_contraseña()