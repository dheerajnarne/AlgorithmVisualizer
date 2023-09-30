class DFS:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        self.check = 0
        for i, j in self.edges:
            if i not in self.graph_dict:
                self.graph_dict[i] = [j]
            else:
                self.graph_dict[i].append(j)

    def algorithmDFS(self, start, end, path=None):
        if path is None:
            path = []
        if self.check == 1:
            return []
        path.append(start)
        if start == end:
            self.check = 1
            return [path]

        if start not in self.graph_dict:
            return []

        sorted_nodes = sorted(self.graph_dict[start])
        paths = []

        for node in sorted_nodes:
            if node not in path:
                new_paths = self.algorithmDFS(node, end, path.copy())
                paths.extend(new_paths)

        return paths

    def showPathDFS(self, start, end):
        paths = self.algorithmDFS(start, end)
        if paths:
            print("Path derived by Depth First Search Algorithm:")
            for path in paths:
                print(" -> ".join(path))
        else:
            print("No valid path found.")

edge = [['S', 'B'], ['S', 'A'], ['A', 'B'], ['B', 'A'], ['A', 'D'], ['D', 'F'], ['B', 'C'], ['C', 'E'], ['F', 'G']]
graphDFS = DFS(edge)
graphDFS.showPathDFS('S', 'G')
