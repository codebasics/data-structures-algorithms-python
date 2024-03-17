# 1. [nyc_weather.csv](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/4_HashTable_2_Collisions/Solution/nyc_weather.csv) 
# contains new york city weather for first few days in the month of January. Write a program that can answer following,
#     1. What was the average temperature in first week of Jan
#     1. What was the maximum temperature in first 10 days of Jan

# Figure out data structure that is best for this problem

#for this problem, I will use an list since I just want the values

with open("/Users/rohansaxena/Desktop/AI Engineer/Week 5&6 - Data Structures and Algorithms in Python/4_HashTable/nyc_weather.csv","r+") as f:
    # create an array for temperatures
    temp_array = []

    #create an array
    for line in f: # for each line in the csv
        # Strip newline characters and then split the line by comma
        tokens = line.strip('\n').split(",")
        #Append the data from the second column wit the values
        temp_array.append(tokens[1])

        #I should have done a try, except loop here to skip the header instead of the process I did

    temp_array.remove('temperature(F)') #remove the header so we now just have the values

    #convert each value from a string into an int
    for val in range(0,len(temp_array)):
        temp_array[val] = int(temp_array[val])

    # 1. What was the average temperature in first week of Jan
    avg_temp = round(sum(temp_array[0:7]) / 7,2)
    print(f"The Average Temp in first week of Jan was {avg_temp} F")

    #1. What was the maximum temperature in first 10 days of Jan

    max_temp = max(temp_array)
    print(f"The Max Temp in first 10 days of Jan was {max_temp} F")

#v2
    
# arr = []

# with open("/Users/rohansaxena/Desktop/AI Engineer/Week 5&6 - Data Structures and Algorithms in Python/4_HashTable/nyc_weather.csv","r") as f:
#     for line in f:
#         tokens = line.split(',')
#         try:
#             temperature = int(tokens[1])
#             arr.append(temperature)
#         except:
#             print("Invalid temperature.Ignore the row")
#     print(arr)
#     print(sum(arr[0:7])/len(arr[0:7]))
#     print(max(arr[0:10]))
