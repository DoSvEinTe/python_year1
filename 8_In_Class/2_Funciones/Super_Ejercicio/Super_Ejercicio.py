# Entrada de datos
rut = input('Ingrese su rut: ')
nombre = input('Ingrese su nombre: ')
dias_trabajados = int(input('Ingrese días trabajados: '))
sueldo_base = int(input('Ingrese el sueldo base: '))
horas_extras = float(input('Ingrese horas extras: '))
carga_familiar = int(input('Ingrese carga familiar: '))

# Definición de constantes
IMM = 165000
MOVILIZACION = 50000
COLACION = 50000

# Procesar los datos con funciones
def valor_dias_trabajados (dias_trabajados, sueldo_base):
    """
    Calcula el valor del sueldo correspondiente a los días efectivamente trabajados.

    Args:
    dias_trabajados (int): Número de días que el trabajador ha laborado en el mes.
    sueldo_base (int): Sueldo base mensual del trabajador.

    Returns:
    float: Valor del sueldo por los días trabajados.
    """
    result = (sueldo_base / 30) * dias_trabajados 
    return result

def valor_gratificacion (IMM):
    """
    Calcula el valor de la gratificación mensual basada en el Ingreso Mínimo Mensual.

    Args:
    IMM (int): Ingreso Mínimo Mensual.

    Returns:
    float: Valor de la gratificación mensual.
    """
    return (IMM * 4.75) / 12


# Llamada de funciones
valor_dia_trabajo = valor_dias_trabajados(dias_trabajados, sueldo_base)
valor_gratif = valor_gratificacion (IMM)

# Salida de los datos
print('\n****************** DATOS DEL TRABAJADOR****************************\n') 

print(f"RUT                   : {rut}") 
print(f"Nombre                : {nombre}")
print(f"Días Trabajados       : {dias_trabajados}")
print(f"Sueldo Base           : {sueldo_base}")
print(f"Horas Extras          : {horas_extras}")
print(f"Carga Familiar        : {carga_familiar}")
print("")
print('****************************IMPONIBLE******************************\n')
print(f"Valor días trabajados :  {valor_dia_trabajo:.2f}")
print(f"Valor gratificación   :  {valor_gratif:.2f}")