# 4. Implement hash table where collisions are handled using linear probing. 
# We learnt about linear probing in the video tutorial. 
# Take the hash table implementation that uses chaining and modify methods to use **linear probing**. 
# Keep MAX size of arr in hashtable as 10.

# default HashTable Class

class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val    


# HashTable Class using Chaining
        
class HashTable2:  
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
            
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))
        
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del",index)
                del self.arr[arr_index][index]
        
# Hash Table Class using probing (keep Max Size at 10) - Rohan's attempt
                
# class HashTable3:  
#     def __init__(self):
#         self.MAX = 10
#         self.arr = [None for i in range(self.MAX)] # you do NOT need each location to be an array of arrays since there is only 1 value per location
        
#     def get_hash(self, key):
#         hash = 0
#         for char in key:
#             hash += ord(char)
#         return hash % self.MAX
    
#     #if the location is empyt, place the value in there
#     #if the location isn't empty, place the value in the next location
#     #if the location is the last value, go to the beginning of the list

#     #go to the beginning of the list, repeat the above logic

#     def __getitem__(self, index): #original method
#         h = self.get_hash(index)
#         return self.arr[h]
    
#     def __setitem__(self, key, val):
#         h = self.get_hash(key) ##this gets you the hash value of your given key
#         found = False
#         if h not in self.arr: #if the hash value does not exist / does not have a value
#             self.arr[h] = val #then place the value in there
#         else: #this means that there is something at that given value
#             if (h+1)<self.MAX: #if h is NOT the last value
#                 self.arr[h+1] = val #then place the value in the next element. This breaks if the next element is full
#             else: #if h is the last value
#                 #start at the beginning of the array and 
#                 for i in range(self.MAX): #for each value of the array
#                     if self.arr[i]=='': #if is empty, then set the value there
#                         self.arr[i] = val
    
#     def __delitem__(self, key):
#         h = self.get_hash(key) ##this gets you the hash value of your given key
#         self.arr[h] = None #set that value to None

# Rohan try 2

class HashTableLinearProbing:
    def __init__(self):
        self.MAX = 10
        self.arr = [None] * self.MAX

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def _probe_for_key(self, key):
        index = self.get_hash(key)
        start_index = index
        while self.arr[index] is not None and self.arr[index][0] != key:
            index = (index + 1) % self.MAX
            if index == start_index:  # We've looped around the entire table
                raise Exception("Hash table is full")
        return index

    def __getitem__(self, key):
        index = self._probe_for_key(key)
        if self.arr[index] is None:
            return None  # Key not found
        return self.arr[index][1]

    def __setitem__(self, key, val):
        index = self._probe_for_key(key)
        self.arr[index] = (key, val)
        
    def __delitem__(self, key):
        index = self._probe_for_key(key)
        if self.arr[index] is None:
            return  # Key not found, nothing to delete
        # Start deletion process
        self.arr[index] = None
        # Rehash items in the following slots until an empty slot is found
        next_index = (index + 1) % self.MAX
        while self.arr[next_index] is not None:
            key_to_rehash, val_to_rehash = self.arr[next_index]
            self.arr[next_index] = None  # Delete the item to rehash it
            self[key_to_rehash] = val_to_rehash  # Re-insert the item
            next_index = (next_index + 1) % self.MAX


t = HashTableLinearProbing()
t["march 6"] = 20
t["march 17"] =  88
print(t.arr)

t["march 17"] = 29
t["nov 1"] = 1

print(t.arr)
print(t["dec 1"])

t["march 33"] = 234
print(t["march 33"])

t["march 33"] = 999
print(t["march 33"])

t["april 1"]=87
t["april 2"]=123
t["april 3"]=234234
t["april 4"]=91
t["May 22"]=4
t["May 7"]=47

# t["Jan 1"]=0

del t["april 2"]

t["Jan 1"]=0
print(t.arr)

                        
