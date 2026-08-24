# Comentario
# Declaración
costo:float = 0
porcentaje_utilidad:float = 0
porcentaje_impuesto:float = 0
monto_utilidad:float = 0
monto_impuesto:float = 0
precio_sin_impuesto:float = 0
precio_total:float = 0

# Entradas
print("Bienvenidos a la calculadora maravillosa")
costo = float(input("Digite el costo"))
porcentaje_utilidad = float(input("Digite el porcentaje de utilidad"))
porcentaje_impuesto = float(input("Digite el porcentaje de impuesto"))


# Procesamiento
monto_utilidad = costo * porcentaje_utilidad
precio_sin_impuesto = costo + monto_utilidad
monto_impuesto = precio_sin_impuesto * porcentaje_impuesto
precio_total = precio_sin_impuesto + monto_impuesto

# Salida
print("Precio total:", precio_total)
print("Monto de utilidad:", monto_utilidad)
print("Monto de impuesto:", monto_impuesto)
