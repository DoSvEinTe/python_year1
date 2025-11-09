from calculos import liquidacionsueldo

#bloque principal
rut=input("Ingresar Rut:")
nombre=input("Ingresar Nombre:")
dt=int(input("Ingresar Dias Trabajados:"))
sb=int(input("Ingresar Sueldo Base:"))
he=int(input("Ingresar Horas Extras:"))
cf=int(input("Ingresar Cargas Familiares:"))
liquidacionsueldo(rut,nombre,dt,sb,he,cf)


