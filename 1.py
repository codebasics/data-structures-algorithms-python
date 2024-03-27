# ### Binary Search Exercise
# 1. When I try to find number 5 in below list using binary search, it doesn't work and returns me -1 index. Why is that?

#     ```numbers = [1,4,6,9,10,5,7]```

# This is because the array is not sorted in order from lowest to highest. 
# Once it splits the first time, it starts looking in the [1,4,6] range and doesn't find 5
    
# 1. Find index of all the occurances of a number from sorted list

#     ```
#     numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
#     number_to_find = 15  
#     ```
#    This should return 5,6,7 as indices containing number 15 in the array

from util import time_it

@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1

@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

#this should run the binary search, find the index, and then recursively run the search on both the right and left side
def binary_search_multiple(numbers_list, number_to_find):

    index = binary_search(numbers_list,number_to_find)
    result_indices = [index]

    # find all indices on the left
    i = index - 1
    while i>=0:
        if numbers_list[i] == numbers_list[index]:
            result_indices.append(i)
        else:
            break
        i = i-1

    # find all indices on the right
    i = index + 1
    while i<len(numbers_list):
        if numbers_list[i] == numbers_list[index]:
            result_indices.append(i)
        else:
            break
        i = i+1

    return sorted(result_indices)

numbers_list = [12, 15, 17, 19, 21, 21, 21, 21, 24, 45, 67]
number_to_find = 21

index = binary_search_multiple(numbers_list, number_to_find)
print(f"Number found at index {index} using binary search")

numbers = [1,4,6,9,11,15,15,15,15,17,21,34,34,56]
number_to_find = 15

index = binary_search_multiple(numbers, number_to_find)
print(f"Number found at index {index} using binary search")

#Lesson: I was approaching it wrong. If something isn't working, scratch the approach. 
#Lesson #2: Try the simplest solution first. Although in this case it's a bit ugly since you're just doing a linear search after your binary search
