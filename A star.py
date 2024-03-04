import math
import heapq

class Node:
    def _init_(self, name):
        self.name = name
        self.adjacent = {}
        self.visited = False
        self.distance = float('inf')
        self.parent = None

    def add_neighbor(self, neighbor, weight):
        self.adjacent[neighbor] = weight

class Graph:
    def _init_(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def get_node(self, name):
        return self.nodes.get(name)

def astar(graph, start, goal):
    open_set = [(0, start)]
    start.distance = 0

    while open_set:
        current_distance, current_node = heapq.heappop(open_set)

        if current_node == goal:
            return reconstruct_path(goal)

        current_node.visited = True

        for neighbor, weight in current_node.adjacent.items():
            tentative_distance = current_node.distance + weight
            if tentative_distance < neighbor.distance:
                neighbor.parent = current_node
                neighbor.distance = tentative_distance
                heapq.heappush(open_set, (tentative_distance + heuristic(neighbor, goal), neighbor))

    return None

def heuristic(node, goal):
    # Heuristic function, Euclidean distance
    x1, y1 = node.name
    x2, y2 = goal.name
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def reconstruct_path(goal):
    path = []
    current = goal
    while current.parent:
        path.append(current)
        current = current.parent
    path.append(current)
    return path[::-1]

# Example usage
if __name__ == "__main__":
    # Create graph
    graph = Graph()
    A = Node((0, 0))
    B = Node((3, 0))
    C = Node((3, 4))
    D = Node((0, 4))
    E = Node((6, 6))

    A.add_neighbor(B, 5)
    A.add_neighbor(C, 10)
    B.add_neighbor(D, 3)
    C.add_neighbor(D, 2)
    D.add_neighbor(E, 7)

    graph.add_node(A)
    graph.add_node(B)
    graph.add_node(C)
    graph.add_node(D)
    graph.add_node(E)

    # Find shortest path
    path = astar(graph, A, E)
    print("Shortest path:", [node.name for node in path])
