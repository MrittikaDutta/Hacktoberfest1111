class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def greedy_coloring(self):
        color_map = {}
        # Sort vertices by their degrees in non-increasing order
        vertices_degrees = [(len(self.graph[i]), i) for i in range(self.V)]
        vertices_degrees.sort(reverse=True)
        
        # Assign colors to vertices
        for _, vertex in vertices_degrees:
            neighbor_colors = {color_map.get(neigh) for neigh in self.graph[vertex]}
            color_map[vertex] = next(color for color in range(self.V) if color not in neighbor_colors)
        
        # Return the number of unique colors used
        return len(set(color_map.values()))


# Example Usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

print(g.greedy_coloring())  # Output: 3
