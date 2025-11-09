#Funcion, Escribe una función que tome una lista de números como entrada y devuelva la suma de esos números

def lista_suma():
    i = 0
    acum = 0
    while i == 0:
        #Entrada de datos
        num = int(input("Ingrese el numero que quiere acumular: "))
        #Acumulacion de numeros
        acum += num
        #Confirmacion
        print("SI = 1")
        print("NO = 0")
        confirm = int(input("¿Desea continuar?: "))

        if confirm < 0 or confirm > 1:
            print("Ingresa un valor valido")
            
        if confirm == 0:
            i = 1

    return acum

resultado = lista_suma()
        
print("La suma de los numeros ingresados es: {}".format(resultado))