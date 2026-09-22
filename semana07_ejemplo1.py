from eii_utils import limpiar_consola, leer_entero

#Variables
edad:int = 0
total:int = 0
i:int = 0
n:int = 0
promedio:float = 0
edades:list [int] = []
diferencias:list [float] = []

#Proceso
limpiar_consola()
n = leer_entero("Digite la cantidad de personas")
edades = [0] * n
diferencias = [0] * n

for i in range(n):
    edad = leer_entero (f"Digite para estudiante {i+1}")
    edades[i] = edad
    total = total + edad

promedio = total / n

for i in range( len(edades)): 
    diferencias[i] = promedio - edades[i]

#Salida
print( "{:.2f}".format(promedio) )
print(edades)
print(diferencias)