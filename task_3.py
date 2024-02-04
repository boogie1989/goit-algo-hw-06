import networkx as nx
from graph import G, streets  # Імпортуємо потрібні бібліотеки і дані


def dijkstra(graph, start):
    # Ініціалізація словників відстаней та шляхів
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0  # Відстань до початкової вершини дорівнює 0
    paths = {node: [] for node in graph.nodes}
    paths[start] = [start]  # Шлях до початкової вершини

    # Створення пустої множини для відстеження відвіданих вершин
    visited = set()

    while visited != set(graph.nodes):
        # Вибираємо вершину з найменшою відстанню, яка ще не була відвідана
        current_node = None
        for node in graph.nodes:
            if node not in visited and (current_node is None or distances[node] < distances[current_node]):
                current_node = node

        # Позначаємо поточну вершину як відвідану
        visited.add(current_node)

        # Оновлюємо відстані та шляхи до сусідніх вершин через поточну вершину
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                weight = graph[current_node][neighbor].get(
                    'weight', 1)  # Вага за замовчуванням дорівнює 1
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    paths[neighbor] = paths[current_node] + [neighbor]

    return distances, paths


# Знаходження найкоротших шляхів від "Main St" до всіх інших вулиць за допомогою самостійно написаного алгоритму Дейкстри
shortest_distances, shortest_paths = dijkstra(G, "Main St")

# Виведення результатів
print("Найкоротші шляхи від 'Main St' до всіх інших вулиць:")
for street in streets:
    if street != "Main St":
        distance = shortest_distances[street]
        path = shortest_paths[street]
        print(f"{street}: Повна відстань = {distance}, Шлях = {path}")
