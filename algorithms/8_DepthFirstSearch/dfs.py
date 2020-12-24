# function for depth first search
def dfs(data, start, visited=set()):

    # if not visited print it
    if start not in visited:
        print(start, end=" ")

    visited.add(start)

    for i in data[start] - visited:

        # if not visited gi in depth of it
        dfs(data, i, visited)
    return


# sample data in dictionary form
data = {
        'A': {'B'},
        'B': {'A', 'C', 'D'},
        'C': {'B', 'E'},
        'D': {'B', 'E'},
        'E': {'C', 'D', 'F'},
        'F': {'E'}
        }


if __name__ == '__main__':

    dfs(data, 'A')
