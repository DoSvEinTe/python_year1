#uso de funciones en python
# metodo procedimental

def presentacion():
    print("Programa que permite carga de 2 valroes por teclado")
    print("Realiza la suma de valores")
    print("Muestra resultado")
    print("*********************************************")

def suma():
    v1=int(input("Ingrese valor 1"))
    v2=int(input("Ingrese valor 2"))
    suma=v1+v2
    print("La suma es:",suma)


def suma2():
  v1=int(input("Ingrese valor 1"))
  v2=int(input("Ingrese valor 2"))
  return v1+v2

def suma3(v1,v2):
    return v1+v2

def suma1(v1,v2):
    suma=v1+v2
    print("La suma es:",suma)


#llamada del metodo
print("PASO 1 PRESENTACION")
presentacion()
print("Paso 2 Suma")
suma()
print("Paso 3 error cuando sumas metodos procedimentales")
"""suma()+suma() esto genera error"""
print("Paso 4 , sumar con parametros de entrada")
v1=int(input("Ingrese valor 1"))
v2=int(input("Ingrese valor 2"))
suma1(v1,v2)
print(suma2())
print("Suma entre metodos",suma2()+suma2())
