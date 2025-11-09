import random

def numero_azar():

    #Asignacion de un numero al azar 1, 10

    azar = random.randint(1, 10)

    #Contador, para que sea 3 oportunidades

    contador = 3

    while contador > 0:
        print("#####################################################################")
        print("")
        num1 = int(input("Ingresa un numero del 1 al 10: "))
       

        if num1 > azar:
            print("El numero ingresado es mayor que el numero random")
        elif num1 < azar:
            print("El numero ingresado es menor que el numero random")
        else:
            print("")
            print("#####################################################################")
            print("")
            print("Felicidades, ese es el numero random")
            print("")
            print("#####################################################################")

            return
        
        contador -= 1

        print("Te quedan {} intentos".format(contador))
        print("")
    
    print("")
    print("Lo siento no te quedan mas intentos, el numero random era {}".format(azar))
    print("")

numero_azar()