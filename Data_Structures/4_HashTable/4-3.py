# 3. [poem.txt](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/4_HashTable_2_Collisions/Solution/poem.txt) 
# Contains famous poem "Road not taken" by poet Robert Frost. 
# You have to read this file in python and print every word and its count as show below. 
#Think about the best data structure that you can use to solve this problem and figure out why you selected that specific data structure.
# ```
#  'diverged': 2,
#  'in': 3,
#  'I': 8

# I am selecting a dictionary (hash table) because I want to store key,value pairs (key being the word, value being the amount of instances)

with open("/Users/rohansaxena/Desktop/AI Engineer/Week 5&6 - Data Structures and Algorithms in Python/4_HashTable/poem.txt","r+") as f:
    #create a dictionary to store each word occurence
    words_dict = {}
    for line in f: # for each line in the file
        tokens = line.split(' ') # split the line into an array each words
        for token in tokens: # for each word in the array of works
            token=token.replace('\n','') # replace \n with nothing
            if token in words_dict: # if the token exists in the dictionary
                words_dict[token]+=1 # increment it's value
            else: #if not
                words_dict[token]=1 #set it's value to 1
    print (words_dict) #print the completed words dict

        


