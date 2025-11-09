#Funcion

def imc(peso, altura):
    imc = peso / (altura * altura)
    return imc

#Declaracion de variables

peso = float(input("Porfavor ingrese su peso: "))
altura = float(input("Porfavor ingrese su altura: "))

#Asigancion de funcion

resultado = imc(peso, altura)

#Impresion de datos

print("#################################################################################")
print("")
print("Considerando que su peso es de {}, y su altura es de {}, se puede decir que su IMC es de {}".format(peso, altura, resultado))
print("")
print("#################################################################################")
