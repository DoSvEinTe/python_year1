#condición compuestas con operadores logicos
n1=float(input("Ingrese valor 1"))
n2=float(input("Ingrese valor 2"))
n3=float(input("Ingrese valor 3"))

if n1>n2 and n1>n3:
    print(n1," Es el mayor")
elif (n2>n3):
    print(n2," Es el mayor")
else:
    print(n3," Es el mayor")

