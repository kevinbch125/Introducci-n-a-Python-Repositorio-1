from eii_utils import leer_entero, leer_texto, limpiar_consola

# Declaración
paciente:str =""
edad:int = 0
encargado:str = ""

# Entradas
limpiar_consola()
paciente= leer_texto ("Digite el nombre del paciente")
edad= leer_entero("Digite la edad: ")

if edad < 18: 
    encargado = leer_texto("Digite el nombre de la persona encargada: ")

# Salidas 

print(f"La persona paciente se llama {paciente} y tiene {edad} años")
print(f"La persona encargada es {encargado}")