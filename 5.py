# ### Merge Sort Exercise

# Modify [merge_sort function](https://github.com/codebasics/data-structures-algorithms-python/blob/master/algorithms/5_MergeSort/merge_sort_final.py) such that it can sort following list of athletes as per the time taken by them in the marathon,
# ```
# elements = [
#         { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
#         { 'name': 'rajab', 'age': 12,  'time_hours': 3},
#         { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
#         { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
#     ]
# ``` 
# merge_sort function should take key from an athlete's marathon log and sort the list as per that key. For example,
# ```
# merge_sort(elements, key='time_hours', descending=True)
# ```
# This will sort elements by time_hours and your sorted list will look like,
# ```
# elements = [
#         {'name': 'rajab', 'age': 12, 'time_hours': 3},
#         {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
#         {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
#         {'name': 'vedanth', 'age': 17, 'time_hours': 1},
#     ]
# ``` 
# But if you call it like this,
# ```
# merge_sort(elements, key='name')
# ```
# output will be,
# ```
# elements = [
#         { 'name': 'chinmay',   'age': 24, 'time_hours': 1.5},
#         { 'name': 'rajab', 'age': 12,  'time_hours': 3},
#         { 'name': 'vedanth',  'age': 17,  'time_hours': 1},
#         { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
#     ]
# ``` 

# [Solution](https://github.com/codebasics/data-structures-algorithms-python/blob/master/algorithms/5_MergeSort/merge_sort_exercise_solution.py)

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return

#     mid = len(arr)//2

#     left = arr[:mid]
#     right = arr[mid:]

#     merge_sort(left)
#     merge_sort(right)

#     merge_two_sorted_lists(left, right, arr)

# def merge_two_sorted_lists(a,b,arr):
#     len_a = len(a)
#     len_b = len(b)

#     i = j = k = 0

#     while i < len_a and j < len_b:
#         if a[i] <= b[j]:
#             arr[k] = a[i]
#             i+=1
#         else:
#             arr[k] = b[j]
#             j+=1
#         k+=1

#     while i < len_a:
#         arr[k] = a[i]
#         i+=1
#         k+=1

#     while j < len_b:
#         arr[k] = b[j]
#         j+=1
#         k+=1

# def merge_two_sorted_by_key(a,b,arr,key):
#     len_a = len(a)
#     len_b = len(b)

#     i = j = k = 0

#     while i < len_a and j < len_b:
#         if a[i][key] <= b[j][key]:
#             arr[k] = a[i]
#             i+=1
#         else:
#             arr[k] = b[j]
#             j+=1
#         k+=1

#     while i < len_a:
#         arr[k] = a[i]
#         i+=1
#         k+=1

#     while j < len_b:
#         arr[k] = b[j]
#         j+=1
#         k+=1

def merge_sort_by_key(arr, key,descending=False):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort_by_key(left,key,descending)
    right = merge_sort_by_key(right,key,descending)

    return merge_two_sorted_lists_by_key(left, right,key,descending)

def merge_two_sorted_lists_by_key(a,b,key,descending):
    sorted_list = []

    len_a = len(a)
    len_b = len(b)

    i = j = 0

    while i < len_a and j < len_b:
        if descending:
            condition = a[i][key] > b[j][key]  # Note the change here for descending
        else:
            condition = a[i][key] <= b[j][key]

        if condition:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    while i < len_a:
        sorted_list.append(a[i])
        i+=1

    while j < len_b:
        sorted_list.append(b[j])
        j+=1

    return sorted_list


elements = [
    { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
    { 'name': 'rajab', 'age': 12,  'time_hours': 3},
    { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
    { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
   ]

print(merge_sort_by_key(elements,key="age",descending=False))