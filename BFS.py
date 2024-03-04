import collections

def bfs(graph, start):
    visited = set()  
    queue = collections.deque([start])  
    visited.add(start)  
    while queue: 
        node = queue.popleft()  
        print(node)  
        for neighbour in graph[node]:
            if neighbour not in visited:  
                visited.add(neighbour) 
                queue.append(neighbour)  

if __name__ == '__main__':
   
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    bfs(graph, 0) 
