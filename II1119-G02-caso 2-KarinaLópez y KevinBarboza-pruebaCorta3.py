from eii_utils import limpiar_consola, leer_flotante, leer_entero, leer_booleano

#Variables
kwh:int = 0
alumbrado:float = 0
bomberos:float = 0
monto:float = 0
iva: float = 0
monto_total: float = 0
#Proceso
limpiar_consola()
kwh = leer_entero("Digite los kwh utilizados")


if kwh <= 30:
    monto= 1744.80
elif kwh <= 200:
    monto= kwh *58.16 
elif kwh <= 300:
    monto= 11632 + (kwh - 200) * 89.24
else:
    monto = 20556 + (kwh - 300) * 92.27 

alumbrado = kwh * 3.02
 
if kwh <= 100:
    bomberos = 0
elif kwh <= 1750:
    bomberos = monto * 0.0175

if kwh <= 280:
    iva = 0
elif kwh >= 280: 
    iva = (monto + alumbrado + bomberos) * 0.13

monto_total = monto + alumbrado + bomberos + iva

print("=" * 50)
print("Desglose de factura électronica (CNFL)")
print("=" * 50)
print(f"Consumo mensual:{kwh:25.2f} kWh")
print("=" * 50)
print(f"Subtotal Energía:          ₡{monto:12.2f}")
print(f"Alumbrado Público:         ₡{alumbrado:12.2f}")
print(f"Tríbuto a Bomberos (1.75%):₡{bomberos:12.2f}")
print(f"Impuesto IVA (13%):        ₡{iva:12.2f}")
print("=" * 50)
print(f"Total a pagar:             ₡{monto_total:12.2f}")
print("=" * 50)