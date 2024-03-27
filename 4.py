# ### Exercise: Insertion Sort

# Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.

# Recall that the median of an even-numbered list is the average of the two middle numbers in a *sorted list*.

# For example, given the sequence `[2, 1, 5, 7, 2, 0, 5]`, your algorithm should print out:

# ```
# 2
# 1.5
# 2
# 3.5
# 2
# 2
# 2
# ```

def find_median_value(elements):
    if len(elements) == 1: #if the array has 1 element
        return elements[0]
    if len(elements) % 2 != 0: #if the array has an odd number of elements
        return elements[(len(elements)//2)]
    else: #if the array has an even number of elements
        return ((elements[int(len(elements)/2)]+elements[int(len(elements)/2-1)])/2)

def insertion_sort(elements):
    for i in range(1, len(elements)):
        print(find_median_value(elements[0:i]))
        anchor = elements[i]
        j = i - 1
        while j>=0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor
    print(find_median_value(elements))

# print (find_median_value([1,2,3,4,5,7,20,33,34]))
# print (find_median_value([1,2,3,4,8,7,20,33]))

elements = [2, 1, 5, 7, 2, 0, 5]
# print(elements[0:1])
insertion_sort(elements)
print(elements)