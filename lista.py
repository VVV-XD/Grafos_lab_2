MAX_VERTICES = 100

class Vertice:
    def __init__(self):
        self.indice = None
        self.rotulo = ""

class ListaAdjacencia:
    def __init__(self):
        self.indice = None
        self.proximo = None

class Grafo:
    def __init__(self):
        self.numVertices = 0
        self.verticeList = [Vertice() for _ in range(MAX_VERTICES)]
        self.rotulos = [[""] * 50 for _ in range(MAX_VERTICES)]
        self.cabecalho = [None] * MAX_VERTICES

    def initGrafo(self):
        self.numVertices = 0
        for i in range(MAX_VERTICES):
            self.cabecalho[i] = None
            self.rotulos[i] = ""

    def adicionaVertice(self, indice, rotulo):
     if 0 <= indice < MAX_VERTICES:
         if self.verticeList[indice].indice is None:
            self.verticeList[indice].indice = indice
            self.numVertices += 1
         self.verticeList[indice].rotulo = rotulo
     else:
        print("Valor inválido!")

    @staticmethod
    def novoNo(indice):
        novo = ListaAdjacencia()
        novo.indice = indice
        novo.proximo = None
        return novo

    def adicionaAresta(self, ver_1, ver_2):
        if 0 <= ver_1 < self.numVertices and 0 <= ver_2 < self.numVertices:
            novo_1 = self.novoNo(ver_2)
            novo_1.proximo = self.cabecalho[ver_1]
            self.cabecalho[ver_1] = novo_1

            novo_2 = self.novoNo(ver_1)
            novo_2.proximo = self.cabecalho[ver_2]
            self.cabecalho[ver_2] = novo_2

            if self.verticeList[ver_1].indice == None:
                self.verticeList[ver_1].indice = ver_1
                self.numVertices += 1
            if self.verticeList[ver_2].indice == None:
                self.verticeList[ver_2].indice = ver_2
                self.numVertices += 1
        else:
            print("Valor inválidos!")

    def removeAresta(self, ver_1, ver_2):
        if 0 <= ver_1 < self.numVertices and 0 <= ver_2 < self.numVertices:
            atual = self.cabecalho[ver_1]
            anterior = None

            while atual != None and atual.indice != ver_2:
                anterior = atual
                atual = atual.proximo

            if atual != None:
                if anterior == None:
                    self.cabecalho[ver_1] = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                del atual

            atual = self.cabecalho[ver_2]
            anterior = None

            while atual != None and atual.indice != ver_1:
                anterior = atual
                atual = atual.proximo

            if atual != None:
                if anterior == None:
                    self.cabecalho[ver_2] = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                del atual
        else:
            print("Valor inválido!")

    def calcularGrau(self, indice):
        grau = 0
        if 0 <= indice < self.numVertices:
            atual = self.cabecalho[indice]
            while atual != None:
                grau += 1
                atual = atual.proximo
        else:
            print("Valor inválido!")
        return grau

    def saoVizinhos(self, indice1, indice2):
        if 0 <= indice1 < self.numVertices and 0 <= indice2 < self.numVertices:
            atual = self.cabecalho[indice1]
            while atual != None:
                if atual.indice == indice2:
                    return True
                atual = atual.proximo
        return False

    def printVertices(self):
        print("Lista de Vértices:")
        for i in range(self.numVertices):
            print("Vértice {}: indice = {}, rotulo = {}".format(i, i, self.rotulos[i]))

    def printGrafo(self):
     print("Grafo:")
     print("Número de Vértices: {}".format(self.numVertices))

     print("Lista de Arestas:")
     for i in range(self.numVertices):
         atual = self.cabecalho[i]
         while atual is not None:
            j = atual.indice
            print("({}, {})".format(i, j), end=" ")
            atual = atual.proximo
         print()

     somaGrau = 0
     imparGrau = 0
     parGrau = 0
     print("Grau de cada Vértice:")
     for i in range(self.numVertices):
        grau = self.calcularGrau(i)
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
    def GrafoBipartido(self,x,y):
            for z in x:
                for w in x:
                    if (z!=w):
                        if(self.saoVizinhos(z,w)== True):
                            return False
            for z in y:
                for w in y:
                    if (z!=w):
                        if(self.saoVizinhos(z,w)== True):
                            return False
          
            for z in x:
                for w in y:
                        if(self.saoVizinhos(z,w)== True):
                            return True

def GrafoCompleto(vertices):
        grafo = Grafo()
        grafo.initGrafo()
        
        for i in range(vertices):
           grafo.adicionaVertice(i,"")
        for i in range(grafo.numVertices):
            for j in range(i,grafo.numVertices):
                if(i!=j):
                    grafo.adicionaAresta(i,j)
        return grafo

def GrafoKRegular(vertices,y):
    if(vertices>y and (vertices*y)%2==0):
        grafo = Grafo()
        grafo.initGrafo()
        
        for i in range(vertices):
           grafo.adicionaVertice(i,"")
        
        for i in range(grafo.numVertices):
            if(grafo.calcularGrau(i)<y):
                for j in range(i+1, (i+1)+(y - grafo.calcularGrau(i)) ):
                        grafo.adicionaAresta(i,j)
    else:
        print("Valor inválido!")       
    return grafo