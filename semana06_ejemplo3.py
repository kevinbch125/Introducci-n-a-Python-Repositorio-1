from eii_utils import limpiar_consola, leer_entero

edad:int = 0
acumulado:int = 0
promedio:float = 0
i:int = 0 
cantidad:int = 0

limpiar_consola()
cantidad = leer_entero("Digite la cantidad de estudiantes")

for i in range(cantidad):
    print(f"Estudiante {i+1}")
    edad = leer_entero("Digite la edad")
    acumulado = acumulado + edad

promedio = acumulado / cantidad

print("Promedio: {:.2f}".format(promedio))