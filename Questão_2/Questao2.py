import pandas as pd
from ImplementacoesGrafosPython import GraphAdjMatrix as GMatrix

import pandas as pd
from ImplementacoesGrafosPython import GraphAdjMatrix as GMatrix

def Bellmann_FordAlgorithm(graph, nodeReference):
    n = graph.n
    D = []       #array d_1i 
    anterior = [] #array anterior(i)

    for i in range(0, n):
        anterior.append(None)  # anterior(i) <- 0
        if i == nodeReference:
            D.append(0)        # d_11 <- 0
        else:
            D.append(float('inf')) # d_1i <- oo, para todo i em V - {1}

    # A = {(j, i) | arco com peso v_ji}
    Edges = {} 
    for j in range(0, n):
        for i in range(0, n):
            if graph.M[j][i] != 0:
                edgeElement = {(j, i): graph.M[j][i]}
                Edges.update(edgeElement)

    for _ in range(n - 1):
        for edge in Edges: 
            j, i = edge
            # enquanto existe (j, i) em A | d_1i > d_1j + v_ji fazer
            if D[j] != float('inf') and D[i] > D[j] + Edges[edge]: 
                # SE a condição do 'enquanto' é satisfeita:
                D[i] = D[j] + Edges[edge]  # d_1i <- d_1j + v_ji
                anterior[i] = j            # anterior(i) <- j

    for edge in Edges:
        j, i = edge
        if D[j] != float('inf') and D[i] > D[j] + Edges[edge]:
            print("AVISO: Grafo contém ciclo negativo!")
            return None, None
    
    return D, anterior

def Bellmann_FordAlgorithm(graph, nodeReference):
    n = graph.n
    D = []
    anterior = []
    
    for i in range(0, n):
        anterior.append(None)  
        if i == nodeReference:
            D.append(0)
        else:
            D.append(float('inf')) 

    Edges = {}
    for j in range(0, n):
        for i in range(0, n):
            if graph.M[j][i] != 0:
                edgeElement = {(j, i): graph.M[j][i]}
                Edges.update(edgeElement)
   
    for _ in range(n - 1):
        for edge in Edges:
            j, i = edge
            if D[j] != float('inf') and D[i] > D[j] + Edges[edge]:
                D[i] = D[j] + Edges[edge]
                anterior[i] = j

    for edge in Edges:
        j, i = edge
        if D[j] != float('inf') and D[i] > D[j] + Edges[edge]:
            print("AVISO: Grafo contém ciclo negativo!")
            return None, None
    
    return D, anterior

if __name__== "__main__":
    Input = []
    with open("graph2.txt", 'r') as input:
        for line in input:
            final_Line = line.strip("\n").split("\t")
            Input.append(final_Line)
    
    inputGraph = pd.DataFrame(Input)
    nodesN = int(inputGraph.iloc[0, 0])
    edgesM = int(inputGraph.iloc[0, 1])
    initialNode = inputGraph.iloc[1:edgesM+1, 0].astype(int).to_list()
    finalNode = inputGraph.iloc[1:edgesM+1, 1].astype(int).to_list()
    costNode = inputGraph.iloc[1:edgesM+1, 2].astype(int).to_list()
    
    graph = GMatrix(nodesN, directed=True)
    for i in range(0, edgesM):
        graph.addEdge(initialNode[i], finalNode[i], costNode[i])
    
    k = 0  # vértice de referência = 0
    D, anterior = Bellmann_FordAlgorithm(graph, k)
    
    if D is None:  
        exit()

    ShortWay06 = [6]
    i = 6
    
    while anterior[i] is not None: 
        ShortWay06.append(anterior[i])
        if anterior[i] == 0:
            break
        i = anterior[i]
    
    stringShortWay06 = ""
    for i in range(len(ShortWay06), 0, -1):
        stringShortWay06 += str(ShortWay06[i-1])
        if i != 1:
            stringShortWay06 += "->"
    # Respostas
    print("Baseado na matriz dada:")
    print(f"    Custo do caminho mínimo do vértice 0 a 6: {D[6]}")
    print(f"    Caminho mínimo realizado do vértice 0 até 6: {stringShortWay06}")
