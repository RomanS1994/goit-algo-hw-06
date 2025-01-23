import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


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


def dfs_recursive(graph, start, visited=None, path=None, parent=None):
    


    if visited is None:
        visited = set()
        path = []
    
    # Додати поточну вершину до відвіданих
    visited.add(start)
    print(f"DFS: visited {start}")
    
    if parent is not None:
        path.append((parent, start))
    
    # Перевіряти чи сусід вже був відвіданий
    for next in graph[start]:
        if next not in visited:  
            dfs_recursive(graph, next, visited, path, start)
    
    return path







def bfs_iterative(graph, start):
    visited, queue = {start}, [start]
    path = []  # Для збереження ребер (шляху)

    while queue:
        vertex = queue.pop(0)
        print(f"BFS: visited {vertex}")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                path.append((vertex, neighbour))  # Додаємо ребро до шляху
    return path  # Повертаємо шлях (або visited, якщо потрібен лише список вершин)




# Виклик функції 
print("DFS результат:")
dfs_path = dfs_recursive(G, 'Steven')
print("DFS шлях:", dfs_path)
print(50 * '-')

print("BFS результат:")
bfs_path = bfs_iterative(G, 'Steven')
print("BFS шлях:", bfs_path)




