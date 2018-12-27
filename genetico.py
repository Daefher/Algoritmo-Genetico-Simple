import random
from operator import itemgetter
from bitstring import BitArray
class Genetico(object):
    """docstring for Genetico."""
    poblacion = None
    func_eval = None
    porcentajeMutacion = 0.2
    def __init__(self,tam):
        self.poblacion = self.initPoblacion(tam)


    def initPoblacion(self,tamaño):
        poblacion = []
        for i in range(0,tamaño):
            rnd = random.randint(1,255)
            cromosoma = BitArray(uint=rnd, length=8)
            poblacion.append(cromosoma)
        return poblacion

    def initGenetico(self):
        evaluados = self.evaluar(self.poblacion)
        cruza = []
        x = 0
        while x < 100000:
            seleccionados = self.seleccion(evaluados)
            for i in range(0,len(seleccionados)-1):
                cruza.append(self.cruza(seleccionados[i][0],seleccionados[i+1][0]))
            evaluados[:] = []
            evaluados = self.evaluar(cruza)
            x += 1
        self.mostrarFinal(evaluados)

    def mostrarPoblacion(self):
        for i in self.poblacion:
            print(i.uint,end='')

    def mostrarFinal(self,lista):
        for i in lista:
            print(i[0].bin)


    def ordenar(self,list):
        return sorted(list, key=itemgetter(1))

    def evaluar(self,lista):
        evaluados = []
        for i in lista:
            valor = (i,self.evaluacion(i))
            evaluados.append(valor)
        return evaluados

    def seleccion(self,lista):
        lista = self.ordenar(lista)
        return lista[5:]

    def cruza(self,cromosomaP, cromosomaM):
        return cromosomaP[:4]+cromosomaM[4:]

    def evaluacion(self,cromosoma):
        return int(cromosoma.uint/2 * random.randint(1,256))
