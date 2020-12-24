# DFS Exercise

![Overview : Employee hierarchy](https://github.com/beladiyadarshan/DFS/blob/main/emp.png?raw=true)

Given a graph containing managers and their employees as a dictionary of sets, print all employees reporting to a given manager.

```
data = {
        "karan": {"darshan","nikhil"},
        "darshan": {"khantil", "tanuj"},
        "tanuj": {"nikhil"},
        "krinish": {"hetul"},
        "khantil" : set(),
        "nikhil" : set()
 }
        
    
 ```
 
 Example: Darshan and Nikhil are reporting to Karan. Khantil and Tanuj are reporting to Darshan.
 
 ```
 Q. Find all employees who are reporting to Karan.
 ```

**Explanation:**

-So here, we want to find all the children nodes of Karan.

-We will perform DFS starting on Karan and then traverse all the children of Karan which are unvisited. 

**Output:**

karan : nikhil darshan tanuj khantil 

[Solution](https://github.com/beladiyadarshan/DFS/blob/main/dfs_exercise.py)
