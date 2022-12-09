def bubblesort(arr,param):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j][param] > arr[j+1][param]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if swapped is False:
            break


elements = [
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
    ]
bubblesort(elements,param="transaction_amount")
print(elements)
