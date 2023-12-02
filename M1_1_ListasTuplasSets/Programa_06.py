""""Nombre: Rene Garcia Soto
    Grupo:951
    Fecha:17/08/23
    Descripcion:Cree una clase llamada Estadística que contiene como atributo una lista de números naturales la cual puede contener repetidos.
    Debe contener los siguientes métodos:
        Frecuencia de Números. Dada la lista, devuelve un diccionario con el número de veces que aparece cada número en la lista.
        Moda. Dada la lista, devuelva la moda de la lista (el valor más repetido). Puedes usar la función anterior como ayuda.
        Histograma. Dada la lista, muestra el histograma de la lista. Puedes reusar los métodos anteriores.
"""


class Estadistica:
    def __init__(self, numeros):
        self.numeros = numeros

    def frecuencia_numeros(self):
        frecuencia = {}
        for numero in self.numeros:
            if numero in frecuencia:
                frecuencia[numero] += 1
            else:
                frecuencia[numero] = 1
        return frecuencia

    def moda(self):
        frecuencia = self.frecuencia_numeros()
        max_frecuencia = max(frecuencia.values())
        moda = [numero for numero, freq in frecuencia.items() if freq == max_frecuencia]
        return moda

    def histograma(self):
        frecuencia = self.frecuencia_numeros()
        for numero, freq in frecuencia.items():
            print(f'{numero}: {"*" * freq}')



numeros = [1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1]
estadistica = Estadistica(numeros)

print("Frecuencia de Números:", estadistica.frecuencia_numeros())
print("Moda:", estadistica.moda())
print("Histograma:")
estadistica.histograma()


