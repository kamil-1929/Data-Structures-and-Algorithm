# Directed Graph
# To implement a directed graph, 
# we simply modify the add_edge method to only add the edge from u to v:

class DirectedGraph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v) # Only add v to u's list
        print(self.graph)
        
    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {', '.join(map(str, self.graph[vertex]))}")

if __name__ == "__main__":
    dg = DirectedGraph()
    dg.add_edge(1,2)
    dg.add_edge(1,3)
    dg.add_edge(2,4)
    dg.add_edge(3,4)
    
    print("\n Directed Graph Adj List:")
    dg.display()