from eii_utils import leer_entero, limpiar_consola, leer_texto

#Declaración
salario:float = 0
salariomin:float = 0
diferencia:float = 0
impuesto:float = 0

limpiar_consola()

salario= leer_texto("Digite su salario")
salariomin= leer_entero("Digite el salario mínimo")

if salario