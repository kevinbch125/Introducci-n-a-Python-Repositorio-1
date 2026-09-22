from eii_utils import limpiar_consola, leer_flotante, leer_entero, leer_booleano

salario_bruto:float = 0
salario_neto:float = 0
renta:float = 0
hijos:int = 0
tiene_conyuge:bool = True
creditos:float = 0
sem:float = 0 
ivm:float = 0
bp:float = 0

limpiar_consola()
salario_bruto = leer_flotante("Digite el salario")
tiene_conyuge = leer_booleano("Tiene conyuge")
hijos = leer_entero("Digite la cantidad de hijos(as)")

if salario_bruto <= 918_000:
    renta = 0
elif salario_bruto <= 1_347_000:
    renta = (salario_bruto - 918_000) * 0.1
elif salario_bruto <= 2_364_000:
    renta = 0 + 42_900 + (salario_bruto - 1_347_00) * 0.15
elif salario_bruto <= 4_727_000: 
    renta = 0 + 42_900 + 152_550 + (salario_bruto - 2_364_000) * 0.2
elif salario_bruto 