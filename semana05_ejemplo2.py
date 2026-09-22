from eii_utils import leer_flotante, leer_booleano, limpiar_consola

# Declaración

monto:float = 0
impuesto:float = 0
es_exoerado:bool = True
total:float = 0

limpiar_consola()

monto= leer_flotante("Digite el monto del producto")
es_exonerado = leer_booleano("El producto es exonerado")

if  es_exonerado:
    impuesto = 0
else:
    impuesto = monto * 0.13

total = monto + impuesto

print(f"Impuesto: {impuesto}")
print(f"Total: {total}")

