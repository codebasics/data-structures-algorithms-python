# # Exercise: Shell Sort

# Sort the elements of a given list using shell sort, but with a slight modification. Remove all the repeating occurances of elements while sorting. 

# Traditionally, when comparing two elements in shell sort, we swap if first element is bigger than second, and do nothing otherwise.

#  In this modified shell sort with duplicate removal, we will swap if first element is bigger than second, and do nothing if element is smaller, but if values are same, we will delete one of the two elements we are comparing before starting the next pass for the reduced gap.



# For example, given the unsorted list `[2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]`, after sorting using shell sort without duplicates, the sorted list would be:

# ```
# [0, 1, 2, 3, 5, 7, 8, 9]
# ```

# [23,3,1,56,34]

def shell_sort(arr):
    size = len(arr)
    gap = size//2

    while gap > 0:
        for i in range(gap,size):
            anchor = arr[i]
            j = i
            while j>=gap and arr[j-gap]>anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2

# [23,3,1,56,34]
        
# def shell_sort_remove_duplicates(arr):
#     size = len(arr)
#     gap = size//2

#     while gap > 0:
#         i = gap
#         while i < size:
#             anchor = arr[i]
#             j = i
#             while j>=gap:
#                 if arr[j-gap] > anchor:
#                     arr[j] = arr[j-gap]
#                 elif arr[j - gap] == anchor:  # If elements are the same, prepare to delete one
#                     del arr[j]  # Delete the current element
#                     size -= 1  # Decrease the size because we've removed an element
#                     i -= 1  # Adjust i since we've shifted the array elements
#                     break  # Exit the inner while loop since we've handled the duplicate
#                 else:
#                     break
#                 j -= gap
#             if j != i:  # Ensures that we don't reset anchor if it was deleted
#                 arr[j] = anchor
#             i += 1
#         gap = gap // 2
        
def shell_sort_remove_duplicates(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap
            
            # Place anchor at its correct position
            arr[j] = anchor

        # After each gap reduction, remove duplicates
        i = 0
        while i < (size - 1):
            # If duplicate found
            if arr[i] == arr[i+1]:
                del arr[i+1]
                size -= 1  # Reduce size after deletion
            else:
                i += 1  # Only increase i if no deletion happened to check next element

        gap = gap // 2

    return arr


tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [5]
    ]

# for elements in tests:
#     shell_sort(elements)
#     print(elements)


elements2 = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
shell_sort_remove_duplicates(elements2)
print(elements2)

elements = [23,12,23,1,1,1,56,34,34]
shell_sort_remove_duplicates(elements)
print(elements)