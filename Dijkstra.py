import heapq

def dijkstra(graph, start, end):
    # Create a dictionary to store shortest distances to nodes
    shortest_distances = {node: float('inf') for node in graph}
    shortest_distances[start] = 0

    # Create a priority queue to store unvisited nodes with their shortest distances
    priority_queue = [(0, start)]

    # Create a dictionary to store the previous node in the shortest path
    previous_nodes = {}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > shortest_distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # Reconstruct the shortest path from end to start
    path = []
    while end:
        path.append(end)
        end = previous_nodes.get(end)

    # Reverse the path to get the correct order from start to end
    return path[::-1] if path[-1] == start else None

# Example usage (Frauenkirche -> Marienplatz)
graph = {
    'A': {'B': 40, 'C': 100, 'D': 172, 'E': 199, 'F': 190},
    'B': {'A': 40, 'C': 63, 'I': 56},
    'C': {'A': 100, 'B': 63, 'D': 40, 'G': 81},
    'D': {'A': 172, 'C': 40, 'K': 74, 'E': 32},
    'E': {'A': 199, 'D': 32, 'F': 18, 'J': 56},
    'F': {'A': 190, 'E': 18, 'H': 64},
    'H': {'F': 64, 'J': 28},
    'J': {'E': 56, 'H': 28, 'K': 34},
    'K': {'J': 34, 'D': 74, 'L': 85},
    'L': {'M': 60, 'G': 139, 'K': 85},
    'M': {'L': 60},
    'G': {'L': 139, 'C': 81, 'I': 60},
    'I': {'B': 56, 'G': 60}
}

start = 'A'
end = 'M'
shortest_path = dijkstra(graph, start, end)

print(f"The shortest path from {start} to {end} is: {shortest_path}")
