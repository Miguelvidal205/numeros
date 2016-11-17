class sumacero():
    def __init__(self, lista):
        self.lista=lista
        self.calcular()
        
    def combinaciones(self,lista, tam):
        pool = tuple(lista)
        n = len(pool)
        if tam > n:
            return
        indices = range(tam)
        yield tuple(pool[i] for i in indices)##es un generador, una lista que esta detenida
        while True:
            for i in range(tam)[::-1]:
                if indices[i] != i + n - tam:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i+1, tam):
                indices[j] = indices[j-1] + 1
            yield tuple(pool[i] for i in indices)##yield es par  crear una lista no inicializada
    def calcular(self):
        c = self.combinaciones(self.lista,3)## aqui hace todos las posibls c
        self.elementos=[i for i in c if sum(i) == 0]
    ##este es el filtro,lista por comprencion, para todas las combinaciones que solo sean = a 0
    def mostrar(self):
        for i in self.elementos:
            print i
            
lista= sumacero([-25,-10,-7,-3,2,4,8,10])
lista.mostrar()

