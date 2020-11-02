def multilevel_selection_sort(elements):
    for x in range(len(elements)):
        min_index = x
        for y in range(x, len(elements)):
            if elements[y]['First Name'] < elements[min_index]['First Name']:
                min_index = y  
        if x != min_index:
            elements[x], elements[min_index] = elements[min_index], elements[x]
    list_of_firstnames=list(set([i['First Name'] for i in elements]))
    for firstname in list_of_firstnames:
        for x in range(len(elements)):
            if elements[x]['First Name']==firstname:
                min_index = x
                for y in range(x, len(elements)):
                    if elements[y]['First Name']==firstname:
                        if elements[y]['Last Name'] < elements[min_index]['Last Name']:
                            min_index = y  
                if x != min_index:
                    elements[x], elements[min_index] = elements[min_index], elements[x]

if __name__ == '__main__':
    elements = [
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

    print(f'Given unsorted array:',*elements,sep='\n')
    multilevel_selection_sort(elements)
    print(f'Array after Multi-Level Sorting:',*elements,sep='\n')


