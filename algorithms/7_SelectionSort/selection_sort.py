
def selection_sort(elements):
    for x in range(len(elements)):
        #Set smallest index unsorted
        minIndex=x
        for y in range(x,len(elements)):
            if elements[y]<elements[minIndex]:##Check if the element at y index is smaller than current minimum
                minIndex=y##Set new Minimum Index
        ##Swap the minimum number with first unsorted number
        if x!=minIndex:
            elements[x],elements[minIndex]=elements[minIndex],elements[x]

if __name__ == '__main__':
    #
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        print(f'Given unsorted array: {elements}')
        selection_sort(elements)
        print(f'Array after Sorting : {elements}')
        print()