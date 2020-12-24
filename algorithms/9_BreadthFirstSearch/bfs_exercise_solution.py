def bfs(data, start, end, visited=[]):
    queue = [start]

    while queue:
        current_node = queue.pop(0)
        if current_node==end:
            print("Path: " + "->".join(visited) + "->" + end)
            return
        visited.append(current_node)

        for i in data[current_node] - set(visited):
            queue.append(i)
    print("Path does not exist!")    
    return


if __name__ == '__main__':
  data = {
    'A': {'B'},
    'B': {'C', 'D'},
    'C': {'E'},
    'D': {'E'},
    'E': {'F'},
    'F': set()
  }
  bfs(data, 'A', 'D')
