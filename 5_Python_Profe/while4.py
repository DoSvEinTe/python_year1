cant=0
x=1
n=int(input("Cuantas piezas cargara:"))
while x<=n:
    largo=float(input("Ingrese la medida de la pieza"))
    if largo>=1.2 and largo<=1.3:
         cant=cant+1  #contar cantidades
    x+=1
print("La cantidad de piezas", cant)
