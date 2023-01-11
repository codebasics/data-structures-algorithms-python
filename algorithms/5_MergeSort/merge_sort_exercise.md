### Merge Sort Exercise

Modify [merge_sort function](https://github.com/codebasics/data-structures-algorithms-python/blob/master/algorithms/5_MergeSort/merge_sort_final.py) such that it can sort following list of athletes as per the time taken by them in the marathon,
```
elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
``` 
merge_sort function should take key from an athlete's marathon log and sort the list as per that key. For example,
```
merge_sort(elements, key='time_hours', descending=True)
```
This will sort elements by time_hours and your sorted list will look like,
```
elements = [
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
    ]
``` 
But if you call it like this,
```
merge_sort(elements, key='name')
```
output will be,
```
elements = [
        { 'name': 'chinmay',   'age': 24, 'time_hours': 1.5},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vedanth',  'age': 17,  'time_hours': 1},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
    ]
``` 

[Solution](https://github.com/codebasics/data-structures-algorithms-python/blob/master/algorithms/5_MergeSort/merge_sort_exercise_solution.py)
