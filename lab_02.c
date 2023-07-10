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

  for (int i = 0 ; i < grafo2B.numVertices ,i++) {
      
      if(grau de grafo vertice i != y){
          
        for (int j = 0; j < y - grau de grafo vertice i  y; j++) {
            
                adicionaAresta2(&grafo2B, i, i+j);
                
        }
      }
    }

  
return grafo2B;
}
