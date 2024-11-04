from collections import deque
import heapq

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")

    def shortest_path(self, start_vertex, end_vertex):
        if start_vertex not in self.graph or end_vertex not in self.graph:
            return None
        
        queue = deque([(start_vertex, [start_vertex])])
        visited = set([start_vertex])
        
        while queue:
            current_vertex, path = queue.popleft()
            
            if current_vertex == end_vertex:
                return path
            
            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None  # If no path found

    def has_cycle(self):
        visited = set()
        
        for vertex in self.graph:
            if vertex not in visited:
                if self._has_cycle_dfs(vertex, visited, -1):
                    return True
        return False
    
    def _has_cycle_dfs(self, vertex, visited, parent):
        visited.add(vertex)
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                if self._has_cycle_dfs(neighbor, visited, vertex):
                    return True
            elif neighbor != parent:
                return True
        return False

    def is_bipartite(self):
        color = {}
        
        for vertex in self.graph:
            if vertex not in color:
                if not self._is_bipartite_bfs(vertex, color):
                    return False
        return True
    
    def _is_bipartite_bfs(self, start_vertex, color):
        queue = deque([start_vertex])
        color[start_vertex] = 0
        
        while queue:
            vertex = queue.popleft()
            current_color = color[vertex]
            
            for neighbor in self.graph[vertex]:
                if neighbor not in color:
                    color[neighbor] = 1 - current_color  # Alternate colors
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    return False  # Same color adjacent node found
        return True


class WeightedGraph(Graph):
    def add_edge(self, vertex1, vertex2, weight=1):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        if vertex1 not in self.graph:
            self.graph[vertex1] = []
        if vertex2 not in self.graph:
            self.graph[vertex2] = []
        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight))  # For undirected graph
    
    def dijkstra(self, start_vertex):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances


# Testing the code
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()

print("\nShortest path from vertex 0 to vertex 3:")
print(g.shortest_path(0, 3))

print("\nDoes the graph contain a cycle?", g.has_cycle())

print("\nIs the graph bipartite?", g.is_bipartite())

# Test Dijkstra's algorithm with the WeightedGraph
wg = WeightedGraph()
wg.add_edge(0, 1, 4)
wg.add_edge(0, 2, 1)
wg.add_edge(1, 2, 2)
wg.add_edge(1, 3, 5)
wg.add_edge(2, 3, 8)
print("\nShortest paths from vertex 0 using Dijkstra's algorithm:")
print(wg.dijkstra(0))
