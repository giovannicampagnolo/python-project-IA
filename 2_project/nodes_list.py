import networkx as nx

def diam_graph(grafo):
    if(grafo.number_of_nodes==0 or grafo.number_of_edges==0 or (not nx.is_connected)):
        return -1
    return nx.diameter(grafo)

def max_degree(grafo):
    nodiVisitati=list(grafo.degree)
    max=0
    for i in range(len(nodiVisitati)):
        if nodiVisitati[i][1] > max:
            max=nodiVisitati[i][1]
    listaNodi=[]
    for i in range(len(nodiVisitati)):
        if(nodiVisitati[i][1]==max):
            listaNodi.append(nodiVisitati[i][0]) 
    return listaNodi

def ampiezza(grafo, start, end):
    if((start not in grafo) or (end not in grafo)):
        return []
    grafo.nodes[start]["visitato"]=True
    grafo.nodes[start]["genitore"]=""
    queue=[start]
    percorso=[]

    while queue:
        nodo=queue.pop(0)
        if(nodo==end):
            while(nodo!=start):
                percorso.append(nodo)
                nodo=grafo.nodes[nodo]["genitore"]
            return [start]+percorso[::-1]
        for neighbor in grafo.neighbors(nodo):
            if(grafo.nodes[neighbor]["visitato"]==False):
                queue.append(neighbor)
                grafo.nodes[neighbor]["visitato"]=True
                grafo.nodes[neighbor]["genitore"]=nodo
    return []