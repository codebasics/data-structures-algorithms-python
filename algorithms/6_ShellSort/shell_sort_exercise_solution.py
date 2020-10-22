def shell_sort(arr):
    n = len(arr)
    div = 2
    gap = n//div
    while gap > 0:
        IndexToDelete = []
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >= temp:
                if arr[j-gap] == temp:
                    IndexToDelete.append(j)
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        IndexToDelete=list(set(IndexToDelete))
        IndexToDelete.sort()
        if IndexToDelete:
            for i in IndexToDelete[-1::-1]:
                del arr[i]
        div *= 2
        n = len(arr)
        gap = n//div


if __name__ == '__main__':
    elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9,  5, 8, 3]

    print(f'Given unsorted list: {elements}')
    shell_sort(elements)
    print(f'List after Sorting : {elements}')

