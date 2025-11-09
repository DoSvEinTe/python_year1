
from calculos import datosTrabajador

rut=input("Rut:")
nombre=input("Nombre:")
dt=int(input("Dias Trabajados:"))
sb=int(input("Sueldo Base:"))
he=float(input("Horas Extras:"))
cf=int(input("Cargas Familiares:"))
datosTrabajador(rut,nombre,dt,sb,he,cf)

