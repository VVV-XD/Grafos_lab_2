import lista, matriz

def GrafoA(x):
        if x == 0:
            grafo = lista.Grafo()
            grafo.initGrafo()

            grafo.adicionaVertice(0, "")
            grafo.adicionaVertice(1, "")  
            grafo.adicionaVertice(2, "")  
            grafo.adicionaVertice(3, "")  

            grafo.adicionaAresta(0, 2)
            grafo.adicionaAresta(0, 3)
            grafo.adicionaAresta(1, 2)
            grafo.adicionaAresta(1, 3) 
            

            grafo.printGrafo()
            if(grafo.GrafoBipartido((0,1),(2,3)) == True ):
                print("O grafo é bipartido.")
            else:
                print("O grafo não é bipartido.")
            print()

            grafoB = lista.GrafoCompleto(5)
            grafoB.printGrafo()
            print()
                
            grafoC = lista.GrafoKRegular(3,2)
            grafoC.printGrafo()
            if(grafoC.GrafoBipartido((0,1),(2))== True ):
                print("O grafo é bipartido.")
            else:
                print("O grafo não é bipartido.")

        elif x == 1:
            grafo2 = matriz.Grafo2()
            grafo2.initGrafo2()

            grafo2.adicionaVertice2(0, "")
            grafo2.adicionaVertice2(1, "")  
            grafo2.adicionaVertice2(2, "")  
            grafo2.adicionaVertice2(3, "")  

            grafo2.adicionaAresta2(0, 2)
            grafo2.adicionaAresta2(0, 3)
            grafo2.adicionaAresta2(1, 2)
            grafo2.adicionaAresta2(1, 3) 
            

            grafo2.printGrafo2()
            if(grafo2.GrafoBipartido2((0,1),(2,3))== True ):
                print("O grafo é bipartido.")
            else:
                print("O grafo não é bipartido.")
            print()

            grafo2B = matriz.GrafoCompleto2(5)
            grafo2B.printGrafo2()
            print()
                
            grafo2C = matriz.GrafoKRegular2(3,2)
            grafo2C.printGrafo2()
            if(grafo2C.GrafoBipartido2((0,1),(2))== True ):
                print("O grafo é bipartido.")
            else:
                print("O grafo não é bipartido.")


if __name__ == "__main__":
    opcao = int(input("Escolha a estrutura de dados (0 - Lista de Adjacência, 1 - Matriz de Adjacência): "))
    
    GrafoA(opcao)
