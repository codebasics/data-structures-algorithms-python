# DFS Exercise

![alt text](https://github.com/beladiyadarshan/Dfs/blob/main/emp.png?raw=true)

Given a Graph in Dictionary Form 

-print all employees who are reporting to given employee

```
Data = {"karan": {"darshan","nikhil"},
        "darshan": {"khantil", "tanuj"},
        'tanuj': {"nikhil"},
        "krinish": {"hetul"},
        "khantil" : set(),
        "nikhil" : set()
        }
        
    
 ```
 
 here darshan and nikhil are reporting to karan and so on....
 
 ```
 Q.find all employees who are reporting to karan
         -do dfs on karan and print all the employees
 ```

**Explanation :**

-so here we wants to find all the childs of karan 

-we will do dfs on karan and then we will traverse all the childs of karan that are not visited 

**output will be :**

karan : nikhil darshan tanuj khantil 

[Solution](https://github.com/beladiyadarshan/Dfs/blob/main/Dfs_exercise.py)


 



