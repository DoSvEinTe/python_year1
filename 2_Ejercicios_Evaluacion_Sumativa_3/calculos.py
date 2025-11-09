imm=460000  # imm=ingreso minimo mensual al dia de hoy 22-04-2026
movilizacion=50000
colacion= 50000

# aqui deben crear los metodos solicitados en la evaluación 3 ya indicados
# 10 puntos
#def ingresar():
 # 10 puntos

def ingresar():
    trabajadores = {}
    continua = "s"

    while continua == "s":
        rut = input("Ingrese su rut: ")
        nombre = input("Ingrese su nombre: ")
        dt = int(input("Ingrese sus dias trabajados: "))
        sb = int(input("Ingrese su sueldo base: "))
        he = float(input("Ingrese sus horas extras: "))
        cf = int(input("Ingrese sus cargas familiares: "))
        
        continua = input("¿Desea continuar? [s/n]: ")

        trabajadores[rut] = (nombre,dt,sb,cf,he)
    return trabajadores

#def imprimirLista(trabajadores):
# 10 puntos 

def imprimirLista(trabajadores):
    print("LISTADO DE TRABAJADORES")
    for i in trabajadores:
        print(i, trabajadores[i][0], trabajadores[i][2], trabajadores[i][3], trabajadores[i][4])

#def imprimirLiquidacion(trabajadores): En este metodo deben recibir el diccionario buscar el rut y los datos pasarlos al metodo liquidacionsueldo(rut,nombre,dt,sb,he,cf)
def imprimirLiquidacion(trabajadores):
    rut = input("Ingrese el RUT del trabajador para generar la liquidación: ")
    if rut in trabajadores:
        nombre, dt, sb, cf, he = trabajadores[rut]
        liquidacionsueldo(rut, nombre, dt, sb, he, cf)
    else:
        print("El RUT ingresado no existe en la lista de trabajadores.")


#################################### NO REALIZAR NINGUNA MODIFICACION DEL CODIGO ###############################################################################################################################

def datostrabajador(rut,nombre,dt,sb,he,cf):
    print("\n\n\n")
    print("****************** LIQUIDACION DE SUELDO POR PANTALLA**************")
    print("\n")
    print("****************** DATOS DEL TRABAJADOR****************************")
    print("Rut\t\t\t:",rut)	
    print("Nombre\t\t\t:",nombre)	
    print("Días Trabajados\t\t:",dt)	
    print("Sueldo Base\t\t:",sb)	 
    print("Numero Horas Extras\t:",he)	
    print("Cargas Familiares\t:",cf)
    print("******************************************************************")

# imponible
def calculodiastrabajados(dt,sb):    
    return round((sb/30)* dt)   

def gratificacion():
    return round((imm*4.75)/ 12)

def Horasextras(he,sb):
    return round(sb*0.007777*he)

def sumaImponible(dt,sb,he):
    return round(calculodiastrabajados(dt,sb)+gratificacion()+Horasextras(he,sb))


# no imponible
def cargafamiliar(nc, imponible):
    tramo=0
    if  imponible<=398443:
        tramo= nc*15597
    else:
        if imponible<=581968:
            tramo= nc*9571
        else:
            if imponible<=907672:
                tramo= nc*3025
            else:
                tramo= 0
    return tramo

# descuentos
def afp(imponible):
    return imponible*(12.75/100)

def fonasa(imponible):
    return imponible*(7/100)

# llamada al metodo liquidacionsueldo desde el metodo imprimirLiquidacion

def liquidacionsueldo(rut,nombre,dt,sb,he,cf):
    datostrabajador(rut,nombre,dt,sb,he,cf)
    sumaimp=sumaImponible(dt,sb,he)
    sumaNoImponible=movilizacion+colacion+cargafamiliar(cf,sumaimp)
    print("****************************IMPONIBLE******************************")
    print("Valor días trabajados\t:",calculodiastrabajados(dt,sb))	
    print("Valor gratificación\t:",gratificacion())	
    print("Valor horas extras\t:",Horasextras(he,sb))
    print("****************************************")
    print("SUMA IMPONIBLE\t\t:",sumaimp)
    print("****************************NO IMPONIBLE******************************")
    print("Valor Movilización\t:",movilizacion)	
    print("Valor colación\t\t:",colacion)	
    print("Valor Carga Familiar\t:",cargafamiliar(cf,sumaimp))
    print("****************************************")
    print("SUMA NO IMPONIBLE\t:",sumaNoImponible)
    print("****************************DESCUENTOS ******************************")
    print("Valor AFP 12,75% \t:",afp(sumaimp))	
    print("Valor FONASA 7% \t:",fonasa(sumaimp))
    sumadescuento=afp(sumaimp)+fonasa(sumaimp)
    print("****************************************")
    print("SUMA DESCUENTO\t\t:",sumadescuento)
    print("****************************TOTAL A PAGAR ******************************")
    total=sumaimp+sumaNoImponible-sumadescuento
    print('VALOR LIQUIDO A PAGAR\t',total)

