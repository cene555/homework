from collections import deque

def dfs(vertex, visited, stack):
    if vertex in visited:
        return
            
    visited.add(vertex)
            
    for neighbor in graph.get(vertex, []):
        dfs(neighbor, visited, stack)        
    stack.appendleft(vertex)

def topological_sort(graph):
    visited = set()
    stack = deque()
    
    for vertex in graph:
        dfs(vertex, visited, stack)
    
    return list(stack)

graph = {
    'C': ['E'],
    'D': ['B'],
    'E': ['C', 'D'],
    'A': ['B', 'C', 'E'],
    'B': ['D', 'C']
    
}

print(topological_sort(graph))
