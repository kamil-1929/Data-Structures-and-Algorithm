# Weighted Graph
# To implement a weighted graph, 
# we can modify the adjacency list to store tuples of (vertex, weight):

class WeightedGraph:
    def __init__(self):
        self.graph = {}
        
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        
        self.graph[u].append((v, weight)) # add (vertex, weight) to to u's list
        self.graph[v].append((u, weight))
        
    def display(self):
        for vertex in self.graph:
            edges = ', '.join(f"{v} (weight:{w})" for v, w in self.graph[vertex])
            print(f"{vertex}: {edges}")


if __name__ == "__main__":
    wg = WeightedGraph()
    wg.add_edge(1,2,5)
    wg.add_edge(2,4,6)
    wg.add_edge(3,2,8)
    wg.add_edge(2,4,3)
    wg.add_edge(3, 4,2)
    
    print("Weighted Graph Adj List:")
    wg.display()