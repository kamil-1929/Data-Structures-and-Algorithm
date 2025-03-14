#Simple Undirected Graph Implementation

# Adding an Edge: O(1) on average (O(V) in the worst case for existence check).
# Displaying the Graph: O(V + E).
# Space Complexity: O(V + E).


class Graph:
    def __init__(self):
        self.graph = {} # dict to store the graph 
    
    def add_edge(self, u, v):
        """Add an edge between vertex u and vertex v"""
        
        if u not in self.graph:
            self.graph[u] = [] # initialize the adj list for u
        
        if v not in self.graph: 
            self.graph[v] = [] # initialize the adj list for v
        
        self.graph[u].append(v) # Add v to u's list
        self.graph[v].append(u) # add u to v's list ( it is undirected)
        print(self.graph)
        
    def display(self):
        for vertex in self.graph:
            print(f"{vertex}:{', '.join(map(str, self.graph[vertex]))}")
    
if __name__ == "__main__":
    g = Graph()
    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(2,4)
    g.add_edge(3,4)
    g.add_edge(4,5) 
    
    print("\n Graph adjacency List:")
    g.display()    





# Graph Class:
# The Graph class uses a dictionary to represent the adjacency list. 
# Each key is a vertex, and the value is a list of adjacent vertices.

# add_edge Method:
# This method adds an edge between two vertices. 
# It updates the adjacency list for both vertices since the graph 
# is undirected.

# display Method:
# This method prints the adjacency list representation of the graph.

