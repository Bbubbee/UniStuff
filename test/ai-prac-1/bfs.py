from collections import deque


"""  
    Breadth First Search.
    
    Visits each and every node in a graph. 
"""


def bfs_traversal(graph, root): 
    # Visited set - we only explore/visit each node once
    visited = set()
    
    # Queue - will hold the root node first
    # This is where we will start searching from
    queue = deque([root])
    
    while queue:
        # Visit the front of the queue
        vertex = queue.popleft()
        visited.add(vertex) 
        
        # Explore the neighbours of the node 
        for neighbour in graph[vertex]:
            
            # Ensure we have not visited this nieghbour node yet
            if neighbour not in visited: 
                queue.append(neighbour)
                
    print(visited) 


def bfs_actual_search(graph, start, target):
    visited = set()
    queue = deque([start])
    
    # Path to goal 
    path: list = []
    path.append(start)
    
    found: bool = False
    
    while queue :
        # Explore node
        vertex = queue.popleft()
        visited.add(vertex) 
        
        # Expand neighbours
        for neighbour in graph[vertex]:

            if neighbour not in visited: 
                queue.append(neighbour)
                
                # Check if 
                if neighbour == target:
                    found = True
                    break
                
                # Expand the neighbours into the queue
                
                
    
        if found: break 
                
    # print(queue) 
        
        
        
    


if __name__ == "__main__":
    # Graph of connected nodes
    graph = { 0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 4], 3: [0], 4: [2] }
    
    bfs_actual_search(graph, 4, 3)
    