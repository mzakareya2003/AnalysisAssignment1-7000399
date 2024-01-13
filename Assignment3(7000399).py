'''
Mohamed Ihab Seifedlin Zakaria 7000399 T2 Analysis Assignment 3

Q1: Given an undirected graph, explain how you can determine whether it is a tree or not?

A1: 2 things we have to check. 
    -First we check if our graph has a cycle or not:
        *We can do this using DFS/BFS while traversing the graph 
            and checking if it has a back edge that forms a cycle.
            
    -Second we check for connectivity:
        A tree must be connected, that it has ONE path between every pair of nodes.
        Use BFS/DFS to find all connections, if it has more than one path it's not a tree'
        
        
    
Q2: What would be the running time?
A2: Time complexity should be O(V+E)
'''
from collections import defaultdict, deque
    
def addEdges(graph, edges):
    for edge in edges:
        u, v = edge
        graph[u].append(v)

def DFS(graph, node, visited, path):
    visited[node] = True
    path.append(node)

    for i in sorted(graph[node]):
        if visited[i] == False:
            DFS(graph, i, visited, path)

    return path

def BFS(graph, start):
    visited = [False]*(max(graph)+1)
    queue = deque([start])
    visited[start] = True
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for i in sorted(graph[node]):
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

    return result

def findCycles(graph):
    cycles = []

    for node in graph:
        visited = [False]*(max(graph)+1)
        cycle = DFS(graph, node, visited, [])
        if len(cycle) > 2:
            cycle.append(cycle[0])
            cycles.append(cycle)

    return cycles


def isBipartite(graph):
    if not graph:
        return True

    colors = {}
    for startNode in graph:
        if startNode not in colors:
            queue = deque([startNode])
            colors[startNode] = 0

            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    if neighbor not in colors:
                        colors[neighbor] = 1 - colors[node]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False

    return True


'define inputs of tree'
edges = [(1, 3), (1, 4), (2, 1), (2, 3), (3, 4), (4, 1), (4, 2)]
'define graph data structure'
graph = defaultdict(list)
'add the edges to our graph'
addEdges(graph, edges)

'call DFS, BFS, findCycles, isBipartite methods with the correct inputs and print outputs'

print("Cycles:", findCycles(graph))

print("DFS:", DFS(graph, 1, [False]*(max(graph)+1), []))

print("BFS:", BFS(graph, 1))

print("Is Bipartite:", isBipartite(graph))