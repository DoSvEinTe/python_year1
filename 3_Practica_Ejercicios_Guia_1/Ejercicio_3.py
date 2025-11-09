# Crear un diccionario en Python que defina como clave el número de documento de una persona y como valor un string con su nombre.
# Desarrollar las siguientes funcionalidades:
# 1) Cargar por teclado los datos de 4 personas.
# 2) Listado completo del diccionario.
# 3) Consulta del nombre de una persona ingresando su número de documento.

# Diccionario vacío
datos = {}

# Ciclo para agregar nuevos elementos
for i in range(4):
    documento = input("Ingrese el numero de su documento: ")
    nombre = input("Ingrese su nombre: ")
    datos[documento] = nombre

# Listado completo del diccionario
print("\nListado completo del diccionario:")
for documento in datos:
    print(f"El numero de documento de {datos[documento]} es {documento}")

# Módulo de consultas
print("\nMODULO DE CONSULTAS")
consulta = input("Ingrese el numero de documento del usuario al cual quiere consultar: ")

# Consulta del nombre de una persona por su número de documento
if consulta in datos:
    print(f"El usuario con el documento {consulta} es: {datos[consulta]}")
else:
    print("El usuario no se encuentra en nuestro sistema")
