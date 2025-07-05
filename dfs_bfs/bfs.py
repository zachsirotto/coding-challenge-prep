# BFS using queue
from collections import deque

def bfs(graph, start):
    visited, queue = set(), deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])
