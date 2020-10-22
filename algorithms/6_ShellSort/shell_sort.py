def shell_sort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2


if __name__ == '__main__':
    #
    tests = [
        [11, 9, 29, 7, 2, 15, 28],
        [3, 7, 9, 11],
        [25, 22, 21, 10, 33, 22],
        [29, 15, 28],
        [6],
        [2, 1, 5, 7, 2, 0, 5]
    ]
    
    for elements in tests:
        print(f'Given unsorted array: {elements}')
        shell_sort(elements)
        print(f'Array after Sorting : {elements}')
