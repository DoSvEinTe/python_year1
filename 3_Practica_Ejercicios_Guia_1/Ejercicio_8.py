# Crear un diccionario en Python que defina como clave el número de documento de una persona y como valor un 
# string con su nombre.
# Desarrollar las siguientes funciones:
# 1) Cargar por teclado los datos de 4 personas.
# 2) Listado completo del diccionario.
# 3) Consulta del nombre de una persona ingresando su número de documento.

def carga_datos():
    # Creación del diccionario vacío
    datos = {}

    # Bucle para preguntar a 4 personas
    for i in range(4):
        documento = int(input("Ingrese su número de documento: "))
        nombre = input("Ingrese su nombre: ")

        # Ingreso de datos al diccionario
        datos[documento] = nombre
    
    return datos

def impresion(datos):
    for i in datos:
        print(f"-{i} es el número de documento de: {datos[i]}")
    

def consulta(datos):

    consulta = int(input("Ingrese el numero de documento de la persona a la cual quiere saber el nombre: "))

    for i in datos:
        if consulta == i:
            print(f"El nombre de la persona con el documento ingresado es: {datos[i]}")
        else:
            print(f"Ese numero de documento no se encuentra en nuestros registros")



# Bloque principal
datos = carga_datos()
impresion(datos)
consulta(datos)
