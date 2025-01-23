import networkx as nx
import matplotlib.pyplot as plt


users = ['Thomas', 'Jessica',  'Nicole', 'Clarence', 'Harold', 'Steven', 'Cindy', 'Chelsea', 'Jose', 'Sarah']



edges = [("Thomas", "Jessica"),
        ("Nicole", "Clarence"),
        ("Cindy", "Sarah"),
        ("Chelsea", "Jose"),
        ("Jose", "Thomas"),
        ("Steven", "Nicole"),
        ("Cindy", "Harold"),
        ("Cindy", "Clarence"),
        ("Chelsea", "Clarence"),
        ("Nicole", "Cindy"),
        ("Cindy", "Chelsea"),
        ("Steven", "Jessica"),
        ("Steven", "Clarence"),
        ("Chelsea", "Steven"),
        ("Steven", "Cindy")]



# Ініціалізація графа
G = nx.Graph()
G.add_nodes_from(users)
# Додавання реберa
G.add_edges_from(edges)



# кількість вершин та ребер
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

# Ступінь центральності
degree_centrality = nx.degree_centrality(G)
print('Ступінь центральності', degree_centrality)


plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True)
plt.show()




