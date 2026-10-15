#Variables
cantidad_deseada:int = 0       
bolsas_bonificacion:int = 0    
inventario_actual:int = 0      
costo_total:int = 0            
ingresos_totales:int = 0       
bolsas_vendidas:int = 0        
bolsas_restantes:int = 0       
utilidad_final:int = 0         
jornada_activa:bool = True    
piso_actual:int = 1            
aula_actual:int = 1            
presencia_seguridad:str = ""
aula_activa:bool = True         
continuar_clientes:str = ""    
cantidad_solicitada:int = 0    
precio_venta:int = 0           

print("=== SIMULADOR DE VENTAS DE PLÁTANOS TOSTADOS ===")

cantidad_deseada = int(input("Ingrese la cantidad de bolsas que desea comprar al proveedor: "))

bolsas_bonificacion = (cantidad_deseada // 12) * 3
inventario_actual = cantidad_deseada + bolsas_bonificacion
costo_total = cantidad_deseada * 600

while piso_actual <= 2 and jornada_activa and inventario_actual > 0:
  aula_actual = 1
  
  while aula_actual <= 10 and jornada_activa and inventario_actual > 0:
    print(f"\n-- Ingresando al Piso {piso_actual}, Aula {aula_actual} --")
    print(f"Inventario actual disponible: {inventario_actual} bolsas")

    presencia_seguridad = input("¿Hay personal de seguridad cerca?(si/no): ").lower()
    if presencia_seguridad == "si":
      print("Personal de seguridad presente. La jornada termina")
      jornada_activa = False
    else:
      aula_activa = True
      while aula_activa and jornada_activa and inventario_actual > 0:
        continuar_clientes = input("¿Hay un cliente interesado en comprar en este aula? (si/no): ").lower()

        if continuar_clientes == "si":
          cantidad_solicitada = int(
              input("Ingrese la cantidad de bolsas que desea el cliente (1, 2 o 3): "))

          if cantidad_solicitada <= inventario_actual:
            if cantidad_solicitada == 1:
              precio_venta = 1100
            elif cantidad_solicitada == 2:
              precio_venta = 1700
            elif cantidad_solicitada == 3:
              precio_venta = 2400
            else:
              precio_venta = 0
              print("Cantidad no válida. Solo se permite 1, 2 o 3 bolsas.")

            if precio_venta > 0:
              inventario_actual -= cantidad_solicitada
              bolsas_vendidas += cantidad_solicitada
              ingresos_totales += precio_venta
              print(f"Venta exitosa. Bolsas restantes: {inventario_actual}")

              if inventario_actual == 0:
                print("Inventario insuficiente")
                jornada_activa = False
          else:
            print("Inventario insuficiente para atender la solicitud de este" " cliente." )
        else:
          aula_activa = False

    if jornada_activa:
      aula_actual += 1

  if jornada_activa:
    piso_actual += 1

bolsas_restantes = inventario_actual
utilidad_final = ingresos_totales - costo_total

print("=========================================")
print(f"Ingresos totales: ₡{ingresos_totales:,}")
print(f"Cantidad total de bolsas vendidas: {bolsas_vendidas}")
print(f"Cantidad de bolsas restantes: {bolsas_restantes}")
print(f"Costo total de inversión: ₡{costo_total:,}")
print(f"Utilidad final: ₡{utilidad_final:,}")
print("=========================================")