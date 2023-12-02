""""Nombre: Rene Garcia Soto
    Grupo:951
    Fecha:17/08/23
    Descripcion: Crear una clase llamada GrupoPensionistas la cual tendrá un único atributo una lista o diccionario de objetos de tipo Pensionista
    (Elija a conveniencia si una lista o diccionario). Cada objeto de Pensionista tiene los siguientes atributos: identificador del pensionista (string),
    un entero que indica la edad y una serie de gastos mensuales que se guardan (lista de enteros). El número de gastos mensuales puede variar entre
    pensionistas. Por ejemplo, el pensionista con identificador '1111A' se llama 'Carlos' tiene 68 años y tiene 3 gastos mensuales de 640, 589 y 573.
"""

class Grupo_Pensionista:
    def __init__(self, identificador, edad, pagos):
        self.identificador = identificador
        self.edad = edad
        self.pagos = pagos
    def calcular_media_pagos(self):
        pagos_list = [int(pago) for pago in self.pagos.split(",")]
        media = sum(pagos_list) / len(pagos_list)
        return media
    def calcular_media_edad_total(self, pensionistas):
        edades = [p.edad for p in pensionistas]
        media_edad_total = sum(edades) / len(edades)
        return media_edad_total
    def __str__(self):
        return f"Identificador: {self.identificador}, Edad: {self.edad}, Pagos: {self.pagos}"
def calculos():
    pensionista1 = Grupo_Pensionista(113, 38, "870,560,255")
    pensionista2 = Grupo_Pensionista(155, 23, "500,200,1500")
    pensionista3 = Grupo_Pensionista(669, 67, "3500,8000,15000")
    pensionistas = [pensionista1, pensionista2, pensionista3]
    media_pagos1 = pensionista1.calcular_media_pagos()
    media_pagos2 = pensionista2.calcular_media_pagos()
    media_pagos3 = pensionista3.calcular_media_pagos()
    media_edad_total = pensionista1.calcular_media_edad_total(pensionistas)
    pensionado_mayor_edad = max(pensionistas, key=lambda p: p.edad)
    pensionado_menor_edad = min(pensionistas, key=lambda p: p.edad)
    media_total = (media_pagos1 + media_pagos2 + media_pagos3) / 3
    mayor_promedio = max(pensionistas, key=lambda p: p.calcular_media_pagos())
    pensionistas_ordenados = sorted(pensionistas, key=lambda p: p.calcular_media_pagos())

calculos()
