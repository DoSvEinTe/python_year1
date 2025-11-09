# Funciones con parámetros con valor por defecto

def titulo_subrayado(titulo,caracter="*"):
    print(titulo)
    print(caracter*len(titulo))

#bloque principal
titulo_subrayado("Sistema Informatica ERP")
titulo_subrayado("Ventas","-")
