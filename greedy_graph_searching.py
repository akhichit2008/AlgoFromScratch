class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = {}

    def add_neighbor(self, neighbor_node, cost):
        self.neighbors[neighbor_node] = cost


class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, node1, node2, cost, bidirectional=True):
        node1.add_neighbor(node2, cost)

        if bidirectional:
            node2.add_neighbor(node1, cost)

    def display_graph(self):
        for node in self.nodes:
            print(f'{node.value} connections:')

            for neighbor, cost in node.neighbors.items():
                print(f'   -> {neighbor.value} (cost: {cost})')

            print()


# ------------------------
# Creating Nodes
# ------------------------

A = GraphNode('A')
B = GraphNode('B')
C = GraphNode('C')
D = GraphNode('D')


# ------------------------
# Creating Graph
# ------------------------

graph = Graph()

graph.add_node(A)
graph.add_node(B)
graph.add_node(C)
graph.add_node(D)


# ------------------------
# Adding Edges
# ------------------------

graph.add_edge(A, B, 2)
graph.add_edge(A, C, 5)
graph.add_edge(A, D, 1)

graph.add_edge(B, C, 3)
graph.add_edge(B, D, 4)

graph.add_edge(C, D, 2)


# ------------------------
# Display Graph
# ------------------------

graph.display_graph()


def GreedyGraphSearch(graph):
    k = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    visited = [graph.nodes[0].value]
    n_nodes = len(graph.nodes)
    route = [graph.nodes[0].value]
    min_idx = 0
    for i in range(n_nodes):
        min = float('inf')
        for neighbor in graph.nodes[min_idx].neighbors:
            if graph.nodes[min_idx].neighbors[neighbor] < min and neighbor.value not in visited:
                min = graph.nodes[min_idx].neighbors[neighbor]
                min_idx = k.find(neighbor.value)
                print('Decided',min_idx)
        route.append(neighbor.value)
        visited.append(neighbor.value)
    for path in route:
        print(path,end=' -> ')

GreedyGraphSearch(graph)
