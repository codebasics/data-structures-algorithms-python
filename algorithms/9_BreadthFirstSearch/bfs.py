def bfs(Data, start, visited=set()):

    queue = [start]
    
    while queue:
        currentnode = queue.pop(0)
        if currentnode not in visited: print(currentnode, end = " ")
        visited.add(currentnode)
        
        for i in Data[currentnode] - visited:
            queue.append(i)
            
    return
        
        
Data = {'A': {'B'},
        'B': {'A', 'C', 'D'},
        'C': {'B', 'E'},
        'D': {'B', 'E'},
        'E': {'C', 'D', 'F'},
        'F': {'E'}}
        
if __name__ == '__main__':
    bfs(Data, 'A')
