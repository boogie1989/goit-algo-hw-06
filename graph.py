import networkx as nx
import random

# Створення графа
G = nx.Graph()

# Додавання вершин (вулиць)
streets = ["Main St", "Oak St", "Pine St",
           "Elm St", "Maple St", "Cedar St", "Birch St"]
G.add_nodes_from(streets)

# Додавання ребер (з'єднань між вулицями)
connections = [("Main St", "Oak St"), ("Main St", "Pine St"), ("Main St", "Elm St"),
               ("Oak St", "Maple St"), ("Pine St",
                                        "Cedar St"), ("Elm St", "Birch St"),
               ("Maple St", "Cedar St"), ("Cedar St", "Birch St")]
               
# G.add_edges_from(connections)
for connection in connections:
    G.add_edge(connection[0], connection[1], weight=random.randint(1, 10))
