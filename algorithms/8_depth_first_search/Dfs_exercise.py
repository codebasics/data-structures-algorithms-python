#function for depth first search
def dfs(Data, start,emp,visited=set()):
    
    #if not visited print it
    if start not in visited:
        print(start,end=" ")
        
        if start==emp:
            print(":",end=" ")
        
    
    visited.add(start)


    for i in Data[start] - visited:
        
        #if not visited go in depth of it
        dfs(Data, i, visited)
        
    return 



#sample data in dictionary form
Data = {"karan": {"darshan","nikhil"},
        "darshan": {"khantil", "tanuj"},
        'tanuj': {"nikhil"},
        "krinish": {"hetul"},
        "khantil" : set(),
        "nikhil" : set()
        }


if __name__ == '__main__':

    dfs(Data, "karan","karan")
