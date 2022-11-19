from constraint import *
import networkx as nx

def sistema3():
    problem = Problem()
    problem.addVariable('x', [10,20,30])
    problem.addVariable('y', [40,50,16])
    problem.addVariable('z', [4,5,16])
    problem.addConstraint(lambda a,b: a < b, ('x','y'))
    problem.addConstraint(lambda a, b, c: a + b + c < 65, ('x','y','z'))
    return problem.getSolution()

def grafo_vincoli(grafo):
    problem = Problem()
    nodes = list(nx.nodes(grafo))
    edges = list(nx.edges(grafo))
    colors=["RED", "GREEN", "BLUE"]
    problem.addVariables(nodes,colors)
    for edge in edges:
        problem.addConstraint(lambda a,b: a!=b, (edge[0],edge[1]))
    sol=problem.getSolution()
    if sol==None:
        sol={}
    return sol

def nqueen(n):
    if(n<4 and n!=1):
        return {}
    problem=Problem()
    rows=list(range(n))
    problem.addVariables(rows, rows)
    for x in rows:
        for y in rows:
            if x < y:
                problem.addConstraint(lambda col1, col2, row1=x, row2=y: abs(row1-row2)!=abs(col1-col2) and col1!=col2, (x,y))
    sol=problem.getSolution()
    if sol==None:
        sol={}
    return sol