import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Ініціалізація графа
G = nx.Graph()

# Додавання ребер з вагами (для розрахунку відстані між Користувачами)
G.add_edge("Thomas", "Jessica", weight=3)
G.add_edge("Nicole", "Clarence", weight=5)
G.add_edge("Cindy", "Sarah", weight=14)
G.add_edge("Chelsea", "Jose", weight=22)
G.add_edge("Jose", "Thomas", weight=8)
G.add_edge("Steven", "Nicole", weight=23)
G.add_edge("Cindy", "Harold", weight=45)
G.add_edge("Cindy", "Clarence", weight=21)
G.add_edge("Chelsea", "Clarence", weight=32)
G.add_edge("Nicole", "Cindy", weight=44)
G.add_edge("Cindy", "Chelsea", weight=31)
G.add_edge("Steven", "Jessica", weight=18)
G.add_edge("Steven", "Clarence", weight=33)
G.add_edge("Chelsea", "Steven", weight=24)
G.add_edge("Steven", "Cindy", weight=21)

# Реалізація алгоритму Dijkstra
def dijkstra(graph, start):
    # Ініціалізація відстаней
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)] 
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Пропускаємо вузли, якщо знайдена більша відстань
        if current_distance > distances[current_vertex]:
            continue

        # Обхід сусідів
        for neighbor, attributes in graph[current_vertex].items():
            weight = attributes['weight']  # Отримання ваги ребра
            distance = current_distance + weight

            # Оновлення найкоротшої відстані
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Виклик Dijkstra для вершини "Steven"
shortest_paths = dijkstra(G, 'Steven')
print("Найкоротші відстані від вершини 'Steven':")
for vertex, distance in shortest_paths.items():
    print(f"{vertex}: {distance}")

# Візуалізація графа
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(
    G, pos, with_labels=True, node_size=700, node_color="lightblue",
    font_size=10, font_weight="bold", width=2
)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)
plt.title('Граф із вагами ребер', fontsize=14)
plt.show()
