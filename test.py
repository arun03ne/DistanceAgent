import heapq


# Graph class to store the graph in an adjacency list format
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))

    def dijkstra(self, start, end):
        # Priority queue to store (distance, vertex)
        queue = [(0, start)]  # (distance from start node, start node)
        distances = {start: 0}
        previous_nodes = {start: None}

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_node == end:
                path = []
                while previous_nodes[current_node] is not None:
                    path.insert(0, current_node)
                    current_node = previous_nodes[current_node]
                path.insert(0, start)
                return path, distances[end]

            for neighbor, weight in self.graph.get(current_node, []):
                distance = current_distance + weight
                if neighbor not in distances or distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))

        return None, float('inf')  # No path found


# Example usage
if __name__ == "__main__":
    graph = Graph()

    # Add some edges (example graph)
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 1)

    start = 'A'
    end = 'C'

    path, distance = graph.dijkstra(start, end)

    print(f"Shortest path from {start} to {end}: {path}")
    print(f"Total distance: {distance}")
