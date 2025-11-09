x = 1     #variable x
suma = 0  #acumulador

while x <= 10:
    valor = int(input("Ingrese un valor: "))
    suma = suma + valor # acumulador
    x += 1 # contador
promedio = suma / 10 # calculo

print("La suma de los 10 valores es: ",suma)
print("El promedio es: ",promedio)

#Bucle while que cumula los valores que le demos, va del 1 al 10 y saca el promedio dividiendo lo acumulado / 10