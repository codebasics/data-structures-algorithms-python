def multilevel_selection_sort(elements,sort_by):
    set_of_indices=set()
    for x in range(len(elements)):
        for kx in (elements[x].keys()):
            set_of_indices.add(kx)
    
    #
    print(set_of_indices)
    #

    set_of_indices.remove(sort_by)

    #
    print(set_of_indices)
    #

    for x in range(len(elements)):
        min_index = x
        for y in range(x, len(elements)):
            if elements[y][sort_by] < elements[min_index][sort_by]:
                min_index = y  
        if x != min_index:
            elements[x], elements[min_index] = elements[min_index], elements[x]
    for indx in set_of_indices:
        list_of_sortby=list(set([i[sort_by] for i in elements]))
        for this_of_sort in list_of_sortby:
            for x in range(len(elements)):
                if elements[x][sort_by]==this_of_sort:
                    min_index = x
                    for y in range(x, len(elements)):
                        if elements[y][sort_by]==this_of_sort:
                            if elements[y][indx] < elements[min_index][indx]:
                                min_index = y  
                    if x != min_index:
                        elements[x], elements[min_index] = elements[min_index], elements[x]
        sort_by=indx

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
    multilevel_selection_sort(elements,'First Name')
    print(f'Array after Multi-Level Sorting:',*elements,sep='\n')


