""""Nombre: Rene Garcia Soto
    Grupo:951
    Fecha:17/08/23
    Descripcion:Diseña una función desencripta(s, clave) que realice la función inversa a la función anterior,
    es decir, reciba un string s y una clave y realice la desencriptación del mensaje en el string devolviendo la cadena desencriptada.
"""


def desencripta(s, clave):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_codificado = clave.lower()

    diccionario_decodificacion = {}
    for i, letra in enumerate(alfabeto_codificado):
        diccionario_decodificacion[letra] = alfabeto[i]

    mensaje_decodificado = ''
    for c in s:
        if c.lower() in diccionario_decodificacion:
            if c.isupper():
                mensaje_decodificado += diccionario_decodificacion[c.lower()].upper()
            else:
                mensaje_decodificado += diccionario_decodificacion[c.lower()]
        else:
            mensaje_decodificado += c

    return mensaje_decodificado

codigo = "Dinwy"
clave = 'ixmrklstnuzbowfaqejdcpvhyg'
mensaje_decodificado = desencripta(codigo, clave)
print(mensaje_decodificado)

