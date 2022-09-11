def how_it_workd(data, start, end, visited=[]):
    queue = [start]

    while queue:
        current_node = queue.pop(0)

        visited.append(current_node)
        print(visited)

        for i in data[current_node] - set(visited):
            print("for looped --> {}".format(i))
            print()
            queue.append(i)

    print("wants the data being bf-searched")
    print(data)


def bfs(data, start, end, visited=[]):
    queue = [start]

    while queue:
        current_node = queue.pop(0)
        if current_node==end:
            print("Path: " + "->".join(visited) + "->" + end)
            return
        visited.append(current_node)

        for i in data[current_node] - set(visited):
            print("for looping -->",i)
            queue.append(i)
    print("Path does not exist!")


if __name__ == '__main__':
  data = {
    'A': {'B'},
    'B': {'C', 'D'},
    'C': {'E'},
    'D': {'E'},
    'E': {'F'},
    'F': set()
  }
  print("how it works")
  how_it_workd(data, "A", "D")
  print("out come")
  bfs(data, 'A', 'D')
