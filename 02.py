def dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start])] 

    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))

def bfs(graph, start, goal):
    visited = set()
    queue = [(start, [start])]  

    while queue:
        (vertex, path) = queue.pop(0)
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                queue.append((neighbor, path + [neighbor]))

graph_dict = {
    'Router': ['TV', 'Switch'],
    'TV': ['Router', 'NAS', 'Laptop'],
    'Switch': ['Router', 'PS4'],
    'NAS': ['TV'],
    'Laptop': ['TV', 'PS4'],
    'PS4': ['Switch', 'Laptop']
}

dfs_path = dfs(graph_dict, "Router", "Laptop")
bfs_path = bfs(graph_dict, "Router", "Laptop")

print("DFS path: ", dfs_path);
print("BFS path: ", bfs_path);

# DFS досліджує граф, заглиблюючись у кожний можливий шлях, поки не досягне тупикової вершини або цільової, 
# що не гарантує, що знайдений шлях буде найкоротшим. Це ми і бачимо на прикладі