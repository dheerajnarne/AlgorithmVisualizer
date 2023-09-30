class HillClimbing:
    def __init__(self, edges):
        self.graph = {}
        self.heuristics = {}
        for start, end in edges:
            self.graph.setdefault(start, []).append(end)
            self.heuristics.setdefault(start, 0)
            self.heuristics.setdefault(end, 0)

    def get_heuristics(self):
        for node in self.heuristics:
            self.heuristics[node] = int(input(f'Enter the Heuristic value for {node}: '))

    def hill_climbing(self, current, goal, path=None):
        if path is None:
            path = []
        path.append(current)
        if current == goal:
            return path
        if current not in self.graph:
            return []

        neighbors = self.graph[current]
        neighbors.sort(key=lambda node: self.heuristics[node])
        for neighbor in neighbors:
            if neighbor not in path:
                new_path = self.hill_climbing(neighbor, goal, path.copy())
                if new_path:
                    return new_path

    def show_path_hill_climbing(self, start, end):
        path = self.hill_climbing(start, end)
        if path:
            print("Path derived by Hill Climbing Algorithm:")
            print(" -> ".join(path))
        else:
            print("No valid path found.")

# Define the edges with updated values
edges = [('S', 'B'), ('S', 'A'), ('A', 'B'), ('B', 'A'), ('A', 'D'), ('D', 'F'), ('B', 'C'), ('C', 'E'), ('F', 'G')]

g1 = HillClimbing(edges)
g1.get_heuristics()
g1.show_path_hill_climbing('S', 'G')
