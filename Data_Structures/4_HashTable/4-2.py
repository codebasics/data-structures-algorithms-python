# 2. [nyc_weather.csv](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/4_HashTable_2_Collisions/Solution/nyc_weather.csv) 
# contains new york city weather for first few days in the month of January. W
#     rite a program that can answer following,
#     1. What was the temperature on Jan 9?
#     1. What was the temperature on Jan 4?

# Figure out data structure that is best for this problem

# for this problem, I will use a dictionary (hash table) because I want to store the key and the value

with open("/Users/rohansaxena/Desktop/AI Engineer/Week 5&6 - Data Structures and Algorithms in Python/4_HashTable/nyc_weather.csv","r+") as f:

    #create a dictionary
    dict = {}

    for line in f: # for each line in the csv
        # Strip newline characters and then split the line by comma
        tokens = line.strip('\n').split(",")
        try:
            dict[tokens[0]] = int(tokens[1])
        except:
            print("Invalid temperature.Ignore the row")

    # 1. What was the temperature on Jan 9?
    
    print(dict['Jan 9'])
    # 1. What was the temperature on Jan 4?
    print(dict['Jan 4'])
        


