# DFS Exercise

![Overview : Employee hierarchy](https://github.com/beladiyadarshan/DFS/blob/main/emp.png?raw=true)

Given a graph in dictionary form, print all employees reporting to given employee.

```
data = {
       "karan": {"darshan","nikhil"},
        "darshan": {"khantil", "tanuj"},
        'tanuj': {"nikhil"},
        "krinish": {"hetul"},
        "khantil" : set(),
        "nikhil" : set()
        }
        
    
 ```
 
 Here, Darshan and Nikhil are reporting to Karan and so on...
 
 ```
 Q.Find all employees who are reporting to Karan
        -perform DFS on Karan and print all the employees
 ```

**Explanation:**

-So here, we want to find all the children of Karan.

-We will perform DFS on Karan and then traverse all the children of Karan which are unvisited. 

**Output:**

karan : nikhil darshan tanuj khantil 

[Solution](https://github.com/beladiyadarshan/DFS/blob/main/DFS_exercise.py)
