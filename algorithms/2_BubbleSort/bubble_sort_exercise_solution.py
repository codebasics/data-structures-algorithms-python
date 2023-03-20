# you can use this to sort strings too
def bubble_sort(elements, key=None):
    size = len(elements)

    for i in range(size-1):
        if key is None:
            print("please enter a key to start search.")
            break
        swapped = False
        breakloop =False
        for j in range(size-1-i):
            if key not in elements[j]:
                breakloop = True
                break
            a = elements[j][key]
            b = elements[j+1][key]
            if a > b:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True
         
         if breakloop:
            print("key is not correct")
            break

        if not swapped:
            break

if __name__ == '__main__':
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    bubble_sort(elements, key='transaction_amount')
    print(elements)
