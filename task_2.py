from graph import G

# Функція для виконання пошуку в глибину (DFS)
def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in set(graph.neighbors(start)) - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])

# Функція для виконання пошуку в ширину (BFS)
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


# Використання DFS і BFS для знаходження шляхів від "Main St" до "Birch St"
dfs_result = list(dfs_paths(G, "Main St", "Birch St"))
bfs_result = list(bfs_paths(G, "Main St", "Birch St"))
