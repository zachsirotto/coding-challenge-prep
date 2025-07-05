# DFS iterative

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
