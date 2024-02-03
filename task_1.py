
import matplotlib.pyplot as plt
import networkx as nx
from graph import G


# Візуалізація графа
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_size=2500,
        node_color="lightblue", font_size=10, font_weight="bold")
plt.title("Модель транспортної мережі міста")


print(f'num nodes: {G.number_of_nodes()}')
print(f'num edges: {G.number_of_edges()}')
print(f'degrees: {G.degree()}')


plt.show()
