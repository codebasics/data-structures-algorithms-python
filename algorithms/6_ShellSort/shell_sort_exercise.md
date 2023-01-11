# Exercise: Shell Sort

Sort the elements of a given list using shell sort, but with a slight modification. Remove all the repeating occurances of elements while sorting. 

Traditionally, when comparing two elements in shell sort, we swap if first element is bigger than second, and do nothing otherwise.

 In this modified shell sort with duplicate removal, we will swap if first element is bigger than second, and do nothing if element is smaller, but if values are same, we will delete one of the two elements we are comparing before starting the next pass for the reduced gap.



For example, given the unsorted list `[2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]`, after sorting using shell sort without duplicates, the sorted list would be:

```
[0, 1, 2, 3, 5, 7, 8, 9]
```


 [Solution](https://github.com/codebasics/data-structures-algorithms-python/blob/master/algorithms/6_ShellSort/shell_sort_exercise_solution.py)