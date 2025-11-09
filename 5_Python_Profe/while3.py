x=1     #variable x
suma=0  #acumulador

while x<=10:
    valor=int(input("Ingrese un valor:"))
    suma=suma+valor # acumulador
    x+=1 # contador
promedio=suma/10 # calculo
print("La suma de los 10 valores es:",suma)
print("El promedio es:",promedio)