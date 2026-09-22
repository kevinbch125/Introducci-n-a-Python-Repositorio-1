from eii_utils import limpiar_consola, leer_entero

nota: int = 0
nota_convertida: str = 0

limpiar_consola ()
nota = leer_entero("Digite su nota")

if nota >= 90:
    nota_convertida = "A"
elif nota >= 80:
    nota_convertida = "B"
elif nota >= 70:
    nota_convertida = "C"
elif nota >= 60:
    nota_convertida = "D"
elif nota <= 60:
    nota_convertida = "F"

print(f"Su nota convertida es: {nota_convertida}")