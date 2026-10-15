
x:int = 0
y:int = 0
plastico1:str = "4123-5555-6666-7777"
plastico2:str = "4123-5555-6666-x"
plastico3:str = "4123-5555-6666-777a"
plastico4:str = "4123555566667777"
plastico5:str = "5123555566667777"

def validar_bloque_númerico(texto:str, inicio:int, fin :int) -> bool:
    es_valido:bool = False
    bloque = texto[inicio:fin]
    es_valido = contar_dígitos(bloque) == 4
    return es_valido

def función_angel(números:list[int], digitos:int) -> list[int]:
    salida:list[int] = []
    for i in números:
        if len(str(i)) == digitos:
            salida.append(i)

        return salida


def es_un_dígito(caracter:str) -> bool:
    return(
            caracter == "1" 
            or caracter == "2" 
            or caracter == "3" 
            or caracter == "4" 
            or caracter == "5" 
            or caracter == "6" 
            or caracter == "7" 
            or caracter =="8" 
            or caracter == "9"
            or caracter == "0"
        )

def contar_dígitos(texto:str) -> int:
    contador:int = 0
    for caracter in texto:
        if es_un_dígito(caracter):
         contador += 1
    return contador


def es_número_valido(plástico:str) -> bool:
    salida:bool = False
    contador:int = 0
    plástico = plástico.strip()
    if plástico[0] == "4" and (len(plástico) == 16 or len (plástico) == 19):
        contador = contar_dígitos(plástico)
        if contador == 16 and len(plástico):
         salida = True
        else: 
            salida = validar_bloque_númerico (plástico, 0,4) and validar_bloque_númerico (plástico, 5,9) and validar_bloque_númerico (plástico, 10,14) and validar_bloque_númerico (plástico, 15, 19)
    return salida


def obtener_mayor(a:int, b:int) -> int:
    if a > b:
        return a
    else:
        return b
if __name__=="__main__":
    x, y = 23, 43
    #print(obtener_mayor(x, y))
    print(plastico1, es_número_valido(plastico1))
    print(plastico2, es_número_valido(plastico2))
    print(plastico3, es_número_valido(plastico3))
    print(plastico4, es_número_valido(plastico4))
    print(plastico5, es_número_valido(plastico5))
    print(función_angel([10,34,45,67,78,89,898,887],3))

