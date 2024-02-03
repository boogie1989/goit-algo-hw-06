import networkx as nx
from graph import G, streets

# Знаходження найкоротшого шляху від "Main St" до всіх інших вершин за допомогою алгоритму Дейкстри
shortest_paths = {street: nx.dijkstra_path(
    G, "Main St", street, weight='weight') for street in streets if street != "Main St"}

# Виведення найкоротших шляхів та їх ваг
shortest_paths_weights = {street: nx.dijkstra_path_length(
    G, "Main St", street, weight='weight') for street in streets if street != "Main St"}

# Виведення результатів
print("Найкоротші шляхи від 'Main St' до всіх інших вершин:")
for street, path in shortest_paths.items():
    print(f"{street}: {path} з вагою {shortest_paths_weights[street]}")
