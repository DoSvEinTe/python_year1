imm=460000  # imm=ingreso minimo mensual al dia de hoy 22-04-2026
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

def liquidacionsueldo(rut,nombre,dt,sb,he,cf):
    datostrabajador(rut,nombre,dt,sb,he,cf)
    sumaimp=sumaImponible(dt,sb,he)
    print("****************************IMPONIBLE******************************")
    print("Valor días trabajados\t:",calculodiastrabajados(dt,sb))	
    print("Valor gratificación\t:",gratificacion())	
    print("Valor horas extras\t:",Horasextras(he,sb))
    print("****************************************")
    print("SUMA IMPONIBLE\t\t:",sumaimp)






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


