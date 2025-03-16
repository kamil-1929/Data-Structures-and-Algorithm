# Depth-First Search (DFS)
# DFS is another algorithm for traversing or searching tree or graph 
# data structures. It starts at a selected node and explores as far as 
# possible along each branch before backtracking.

# Exploration Order: Explores as far down a branch as possible before 
# backtracking.
# Data Structure: Can be implemented using a stack (or recursion).
# Time Complexity: O(V + E), where V is the number of vertices and E 
# is the number of edges.
# Space Complexity: O(V) in the worst case, due to the recursion 
# stack or the stack used for iterative implementation.

# Iterative Version:
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    
if __name__ == "__main__":
    # Example graph represented as an adjacency list
    graph = {
        1: [2, 3],
        2: [1, 4, 5],
        3: [1, 6],
        4: [2],
        5: [2, 7],
        6: [3],
        7: [5]
    }
    print("\nDFS starting from vertex 1 (iterative):")
    dfs_iterative(graph, 1)


#Recursive Version:
def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=' ')
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor,visited)

if __name__ == "__main__":
    graph = {
        1: [2,3],
        2: [1,4,5],
        3: [1,6], 
        4: [2],
        5: [2, 7],
        6: [3],
        7:[5]
        }            
    print("\n DFS starting from vertex 1(recursive)")
    dfs_recursive(graph, 1)