class BranchAndBoundWithCostAndHeuristics:
    def __init__(self, edges, oracle):
        self.edges = edges
        self.graph_dict = {}
        self.heuristics = {}
        self.best_path = None
        self.oracle = oracle

        for start, end, cost in self.edges:
            self.graph_dict.setdefault(start, []).append((end, cost))

        for node in oracle[1:]:
            self.heuristics[node] = 0

        self.get_heuristics()

    def get_heuristics(self):
        for node in self.heuristics:
            self.heuristics[node] = int(input(f'Enter the Heuristic value for {node}: '))

    def branch_and_bound(self, start, end, path=None, cost=0):
        if path is None:
            path = []
        path = path + [start]

        if start == end:
            if self.oracle[0] is None or cost == self.oracle[0]:
                self.oracle[0] = cost
                if self.best_path is None or cost < self.best_path[0]:
                    self.best_path = (cost, path.copy())
            return

        if start not in self.graph_dict:
            return

        for neighbor, edge_cost in sorted(self.graph_dict[start], key=lambda x: x[1] + self.heuristics.get(x[0], 0)):
            if neighbor not in path:
                self.branch_and_bound(neighbor, end, path.copy(), cost + edge_cost)

    def show_paths(self, start, end):
        self.branch_and_bound(start, end)

        if self.best_path is not None:
            cost, path = self.best_path
            path.pop(0)
            print("Path derived by Branch And Bound Using Cost and Heuristics Algorithm:")
            print(" -> ".join(map(str, path)))
        else:
            print("No valid path found.")


# Define the edges and oracle with updated values
edges_with_cost = [('S', 'B', 4), ('S', 'A', 3), ('A', 'B', 2), ('B', 'A', 2),
                   ('A', 'D', 4), ('D', 'F', 2), ('B', 'C', 5), ('C', 'E', 6), ('F', 'G', 1)]
oracle_values = [10]

# Create a BranchAndBoundWithCostAndHeuristics object and find the paths
bnbch = BranchAndBoundWithCostAndHeuristics(edges_with_cost, oracle_values)
bnbch.show_paths('S', 'G')
