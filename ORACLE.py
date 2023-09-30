class Oracle:
    def __init__(self, edges):
        self.graph_dict = {}
        for start, end, cost in edges:
            self.graph_dict.setdefault(start, []).append((end, cost))

    def algorithmOracle(self, start, end, path=None, cost=0):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [(cost, path)]

        if start not in self.graph_dict:
            return []

        paths = []
        for neighbor, edge_cost in self.graph_dict[start]:
            if neighbor not in path:
                new_paths = self.algorithmOracle(neighbor, end, path.copy(), cost + edge_cost)
                paths.extend(new_paths)

        return paths

    def showPathsOracle(self, start, end):
        paths = self.algorithmOracle(start, end)

        if not paths:
            print("No valid path found.")
            return

        paths.sort(key=lambda x: x[0])

        print("Paths ranked from best to worst based on cost: ")
        oracle = paths[0]
        print("Oracle:", oracle)


# Define the edges with updated values
edges_with_cost = [('S', 'B', 5), ('S', 'A', 4), ('A', 'B', 3), ('B', 'A', 3),
                   ('A', 'D', 5), ('D', 'F', 2), ('B', 'C', 4), ('C', 'E', 5), ('F', 'G', 1)]

graphOracle = Oracle(edges_with_cost)
graphOracle.showPathsOracle('S', 'G')
