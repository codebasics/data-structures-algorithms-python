# Exercise: Selection Sort

Implement a Milti-Level Sort of a given list of dictionaries. A single dictionary entry contains two keys 'First Name' and 'Last Name'. the list should be sorted first based on 'First Name', then based on 'Last Name', w.r.t. common/same 'First Name' entries.



For example, given the sequence List:
 
```
[
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]
```


Your algorithm should generate sorted list:

```
[
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
    {'First Name': 'Armaan', 'Last Name': 'Dadra'}
    {'First Name': 'Armaan', 'Last Name': 'Kumar'}
    {'First Name': 'Ingrid', 'Last Name': 'Galore'}
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'}
    {'First Name': 'Jade', 'Last Name': 'Canary'}
    {'First Name': 'Jaya', 'Last Name': 'Seth'}
    {'First Name': 'Jaya', 'Last Name': 'Sharma'}
    {'First Name': 'Karan', 'Last Name': 'Kumar'}
    {'First Name': 'Kiran', 'Last Name': 'Kamla'}
    {'First Name': 'Raj', 'Last Name': 'Nayyar'}
    {'First Name': 'Raj', 'Last Name': 'Sharma'}
    {'First Name': 'Raj', 'Last Name': 'Thakur'}
    {'First Name': 'Suraj', 'Last Name': 'Sharma'}
]
```





 [Solution](https://github.com/codebasics/data-structures-algorithms-python/blob/master/algorithms/7_SelectionSort/selection_sort_exercise_solution.py)