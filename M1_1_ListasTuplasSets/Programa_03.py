""""Nombre: Rene Garcia Soto
    Grupo:951
    Fecha:17/08/23
    Descripcion:Diseñe una función encripta(s, codigo), que reciba un string s con un mensaje y un string con una codigo de codificación,
     y retorne el mensaje codificado según la codigo leída. Los signos de puntuación y dígitos que aparecen en el mensaje deben conservarse sin cambios.
"""


def encripta(s, codigo):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    print(len(alfabeto))
    codificacion = {codigo[i]: alfabeto[i] for i in range(26)}
    resultado = []
    for letra in s:
        if letra.isalpha():
            if letra.islower():
                resultado.append(codificacion[letra])
            else:
                resultado.append(codificacion[letra.lower()].upper())
        else:
            resultado.append(letra)

    return ''.join(resultado)


codigo = 'ixmrklstnuzbowfaqejdcpvhyg'
texto = 'Tainy'
texto_codificado = encripta(texto, codigo)
print(texto_codificado)

