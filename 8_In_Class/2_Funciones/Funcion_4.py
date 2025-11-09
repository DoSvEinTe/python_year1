#Funcion, Programa que calcule la tabal de multiplicar de cualquier numero entero dado por el usuario, debe calcular la tabala desde el 0 hasta el 12

def tabla_multiplicar(num1):
    for i in range(0, 13):
        print("{} x {} = {}".format(num1, i, i * num1))

#Entrada de datos

num1 = int(input("Ingrese el numero que quiere multiplicar: "))

#Salida de datos

print("################################# " + "TABLA DE {} ".format(num1) + " #################################")
print("")

tabla_multiplicar(num1)