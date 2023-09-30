import heapq

class BeamSearch:
    def __init__(self, edges, beam_width):
        self.edges = edges
        self.graph = {}
        self.beam_width = beam_width
        self.path_found = False

        for start, end, cost in edges:
            if start not in self.graph:
                self.graph[start] = []
            self.graph[start].append((end, cost))

    def find_path(self, start_node, end_node):
        open_list = [(0, start_node, [])]  # (Total cost, Current node, Path)
        while open_list:
            open_list.sort(key=lambda x: x[0])  # Sort the open list by total cost
            open_list = open_list[:self.beam_width]  # Select top 'beam_width' nodes

            new_open_list = []

            for total_cost, current_node, path in open_list:
                if current_node == end_node:
                    path.append(current_node)
                    return path

                for neighbor, cost in self.graph.get(current_node, []):
                    new_total_cost = total_cost + cost
                    new_path = path + [current_node]
                    new_open_list.append((new_total_cost, neighbor, new_path))

            open_list = new_open_list

        return []

    def show_path(self, start_node, end_node):
        path = self.find_path(start_node, end_node)
        if path:
            print("Path derived by Beam Search Algorithm:")
            print(" -> ".join(path))
        else:
            print("No valid path found.")

# Define the edges
edges = [('S', 'A', 2), ('S', 'B', 3), ('A', 'B', 1), ('B', 'A', 1),
         ('A', 'D', 2), ('D', 'F', 1), ('B', 'C', 2), ('C', 'E', 3), ('F', 'G', 1)]

# Create a BeamSearch object and find the path with a beam width of 2
beam_search = BeamSearch(edges, beam_width=2)
beam_search.show_path('S', 'G')
