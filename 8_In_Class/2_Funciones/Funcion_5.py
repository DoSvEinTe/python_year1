def presentacion():
    print("Programa que permite carga de 2 valores por teclado")
    print("Realiza la suma de valores")
    print("Muestra resultado")
    print("####################################################")

def suma():
    v1 = int(input("Ingrese valor 1: "))
    v2 = int(input("Ingrese valor 2: "))
    suma = v1 + v2
    print("La suma es: ", suma)

#llamada de metodo

presentacion()
suma()

#suma() + suma() esto genera error