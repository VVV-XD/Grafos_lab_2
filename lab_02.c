
Grafo GrafoCompleto(int x) {
Grafo2 grafo2B;
initGrafo2(&grafo2B);

  // Adicionando vértices para formar um grafo2 completo
    for (int i = 0; i < x; i++) {
        adicionaVertice2(&grafo2B,i,""); 
    }

   // Adicionando arestas para formar um grafo2 completo
    for (int i = 0; i < grafo2B.numVertices; i++) {
        for (int j = i; j < grafo2B.numVertices; j++) {
            if (i != j) {
                adicionaAresta2(&grafo2B, i, j);
            }
        }
    }
return grafo2B;
}


Grafo GrafoKCompleto(int x,int y) {
 Grafo2 grafo2B;
 initGrafo2(&grafo2B);

  // Adicionando vértices 
    for (int i = 0; i < x; i++) {
        adicionaVertice2(&grafo2B,i,""); 
    }

   // Adicionando arestas 
// Adicionando arestas para formar um grafo2 completo
    for (int i = 0; i < grafo2B.numVertices; i++) {
        for (int j = i; j < grafo2B.numVertices; j++) {
            if (i != j) {
                adicionaAresta2(&grafo2B, i, j);
            }
        }
    }

  for (int z = x-1 ,int i = 0 ; i < grafo2B.numVertices && z > y; z++,i--) {
        for (int j = 0; j < grafo2B.numVertices; j++) {
            if (i != j) {
                remove arestaAresta2(&grafo2B, i, j);
            }
        }
    }

  
return grafo2B;
}
