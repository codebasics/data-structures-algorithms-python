# BFS_Traversal
BFS Traversal of a graph in python using graph given in dictionary

Implement a program to find whether a path exists for an airline route or not. The routes are described using graph having nodes. The names of the graphs are named alphabet characters for easy understanding. Print the path if it exists; print the denying statement if it doesn't!

Example: A, B, C, D, E, F are the nodes of the graph.


For example, you are given following data: 

```
data = {'A': {'B'},
        'B': {'A', 'C', 'D'},
        'C': {'B', 'E'},
        'D': {'B', 'E'},
        'E': {'C', 'D', 'F'},
        'F': {'E'}}
```

the resultant graph will be :-

![alt text](https://github.com/nikhilailani/data-structures-algorithms-python/blob/master/algorithms/9_BreadthFirstSearch/DFS_BFS_Graph.png)


**Explanation:** Here, selecting A as source node and D as destination node, the values are passed to the function.

Your output should look like this:

'''
Path exists!
Path : A->B->D
'''

[Solution](https://github.com/nikhilailani/data-structures-algorithms-python/blob/master/algorithms/9_BreadthFirstSearch/DFS_BFS_Graph.pngbfs_exercise_solution.py)
