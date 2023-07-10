
MAX_VERTICES = 100

class Vertice:
    def __init__(self):
        self.indice = None
        self.rotulo = ""

class Grafo2:
    def __init__(self):
        self.vertices = [[0] * MAX_VERTICES for _ in range(MAX_VERTICES)]
        self.numVertices = 0
        self.verticeList = [Vertice() for _ in range(MAX_VERTICES)]

    def initGrafo2(self):
        self.numVertices = 0
        for i in range(MAX_VERTICES):
            for j in range(MAX_VERTICES):
                self.vertices[i][j] = 0

    def adicionaVertice2(self, indice, rotulo):
        if self.numVertices < MAX_VERTICES:
            vertice = Vertice()
            vertice.indice = indice
            vertice.rotulo = rotulo

            self.verticeList[self.numVertices] = vertice
            self.numVertices += 1
        else:
            print("Limite máximo de vértices atingido!")

    def adicionaAresta2(self, ver_1, ver_2):
        if 0 <= ver_1 < self.numVertices and 0 <= ver_2 < self.numVertices:
            self.vertices[ver_1][ver_2] += 1

            if ver_1 != ver_2:
                self.vertices[ver_2][ver_1] += 1
        else:
            print("Valor inválido!")

    def removeAresta2(self, ver_1, ver_2):
        if 0 <= ver_1 < self.numVertices and 0 <= ver_2 < self.numVertices:
            self.vertices[ver_1][ver_2] = 0
            self.vertices[ver_2][ver_1] = 0
        else:
            print("Valor inválido!")

    def calcularGrau2(self, indice):
        grau = 0
        if 0 <= indice < self.numVertices:
            for i in range(self.numVertices):
                if self.vertices[indice][i] == 1:
                    grau += 1
                if self.vertices[indice][i] == 2:
                    grau += 2
        else:
            print("Valor inválido!")
        return grau

    def saoVizinhos2(self, indice1, indice2):
        if 0 <= indice1 < self.numVertices and 0 <= indice2 < self.numVertices:
            if self.vertices[indice1][indice2] == 1 and self.vertices[indice2][indice1] == 1:
                return True
        return False

    def printVertices2(self):
        print("Lista de Vértices:")
        for i in range(self.numVertices):
            print("Vértice {}: indice = {}, rotulo = {}".format(i, self.verticeList[i].indice, self.verticeList[i].rotulo))

    def printGrafo2(self):
        print("Grafo2:")
        print("Número de Vértices: {}".format(self.numVertices))

        print("Lista de Arestas:")
        for i in range(self.numVertices):
            for j in range(self.numVertices):
                if self.vertices[i][j] >= 1:
                    print("({}, {})".format(i, j), end=" ")
            print()

        somaGrau = 0
        imparGrau = 0
        parGrau = 0
        print("Grau de cada Vértice:")
        for i in range(self.numVertices):
            grau = self.calcularGrau2(i)
            print("Vértice {}: Grau = {}".format(i, grau))
            somaGrau += grau
            if(grau%2 == 1):
                imparGrau += 1
            if(grau%2 == 0):
                parGrau += 1

        numArestas = somaGrau // 2
        print("Número de Arestas: {}".format(numArestas))
        print("Número da somatório dos Graus: {}".format(somaGrau))
        print("Número dos Graus impares: {}".format(imparGrau))
        print("Número dos Graus pares: {}".format(parGrau))

# Lista2

    def GrafoBipartido2(self,x,y):
        for z in x:
            for w in x:
                if (z!=w):
                    if(self.saoVizinhos2(z,w)== True):
                        return False
        for z in y:
            for w in y:
                if (z!=w):
                    if(self.saoVizinhos2(z,w)== True):
                        return False
          
        for z in x:
            for w in y:
                    if(self.saoVizinhos2(z,w)== True):
                        return True
                
       


def GrafoCompleto2(vertices):
        grafo = Grafo2()
        grafo.initGrafo2()
        
        for i in range(vertices):
           grafo.adicionaVertice2(i,"")
        for i in range(grafo.numVertices):
            for j in range(i,grafo.numVertices):
                if(i!=j):
                    grafo.adicionaAresta2(i,j)
        return grafo

def GrafoKRegular2(vertices,y):
    if(vertices>y and (vertices*y)%2==0):
        grafo = Grafo2()
        grafo.initGrafo2()
        
        for i in range(vertices):
           grafo.adicionaVertice2(i,"")
        
        for i in range(grafo.numVertices):
            if(grafo.calcularGrau2(i)<y):
                for j in range(i+1, (i+1)+(y - grafo.calcularGrau2(i)) ):
                        grafo.adicionaAresta2(i,j)
    else:
        print("Valor inválido!")       
    return grafo


        
        
        
                       
       
