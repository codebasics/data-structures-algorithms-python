def multilevel_selection_sort(elements, sort_by_list):
    for sort_by in sort_by_list[-1::-1]:
        for x in range(len(elements)):
            min_index = x
            for y in range(x, len(elements)):
                if elements[y][sort_by] < elements[min_index][sort_by]:
                    min_index = y
            if x != min_index:
                elements[x], elements[min_index] = elements[min_index], elements[x]


if __name__ == '__main__':
    elements = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar', 'Middle Name': 'B'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma', 'Middle Name': ''},
        {'First Name': 'Karan', 'Last Name': 'Kumar', 'Middle Name': ''},
        {'First Name': 'Jade', 'Last Name': 'Canary', 'Middle Name': ''},
        {'First Name': 'Raj', 'Last Name': 'Thakur', 'Middle Name': 'A'},
        {'First Name': 'Raj', 'Last Name': 'Sharma', 'Middle Name': 'A'},
        {'First Name': 'Kiran', 'Last Name': 'Kamla', 'Middle Name': ''},
        {'First Name': 'Armaan', 'Last Name': 'Kumar', 'Middle Name': ''},
        {'First Name': 'Jaya', 'Last Name': 'Sharma', 'Middle Name': ''},
        {'First Name': 'Ingrid', 'Last Name': 'Galore', 'Middle Name': ''},
        {'First Name': 'Jaya', 'Last Name': 'Seth', 'Middle Name': ''},
        {'First Name': 'Armaan', 'Last Name': 'Dadra', 'Middle Name': ''},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick', 'Middle Name': ''},
        {'First Name': 'Aahana', 'Last Name': 'Arora', 'Middle Name': ''}
    ]

    print(f'Given unsorted array:', *elements, sep='\n')
    multilevel_selection_sort(
        elements, ['First Name', 'Last Name'])
    print(f'Array after Multi-Level Sorting:', *elements, sep='\n')
