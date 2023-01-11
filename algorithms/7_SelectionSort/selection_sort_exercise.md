# Exercise: Selection Sort

Implement a Multi-Level Sort of a given list of dictionaries based on a given sorting order. If user wants to sort dictionary based on First Key 'A', Then Key 'B', they shall pass list of keys in the order of  preference as a list ['A','B']. Your code should be able to sort list of dictionaries for any number of keys in sorting order list.

Using this multi-level sort, you should be able to sort any list of dictionaries based on sorting order preference

Example:
A single dictionary entry contains two keys 'First Name' and 'Last Name'. the list should be sorted first based on 'First Name', then based on 'Last Name', w.r.t. common/same 'First Name' entries.

for this, one shall past sorting order of preference list [ 'First Name' , 'Last Name' ]

For this, Given the following sequence List:
 
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