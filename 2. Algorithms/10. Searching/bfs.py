# Breadth-First Search (BFS)
# BFS is an algorithm for traversing or searching tree or graph 
# data structures. It starts at a selected node (often called the "root" 
# in trees) and explores all of its neighbors at the present depth prior 
# to moving on to nodes at the next depth level.

# Characteristics of BFS:
# Exploration Order: Explores all neighbors of a node before moving to the
# next level.
# Data Structure: Uses a queue to keep track of nodes to be explored.
# Time Complexity: O(V + E), where V is the number of vertices and E is 
# the number of edges.
# Space Complexity: O(V) in the worst case, as it may store all vertices 
# in the queue.

from collections import deque
def bfs(graph, start):
    visited = set() # keep track of visited nodes
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        #Enqueue all unvisited neighbors
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        
if __name__ == "__main__":
    graph = {
        1: [2,3],
        2: [1,4,5],
        3: [1,6],
        4: [2],
        5: [2,7],
        6: [3],
        7: [5]
    }
    print("BFS starting the vertex 1: ")
    bfs(graph, 1)