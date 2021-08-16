elements = [
    {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
    {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
    {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
    {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'}, ]


def bubble_sort(elements, key):
    result = []
    if key == 'name':
        for i in range(len(elements)):
            result.append(elements[i]['name'])
    elif key == 'transaction_amount':
        for i in range(len(elements)):
            result.append(elements[i]['transaction_amount'])
    elif key == 'device':
        for i in range(len(elements)):
            result.append(elements[i]['device'])
    else:
        print('> invalid \'KEY\' input')
    result.sort()

    try:
        result2 = []
        for i in range(len(elements)):
            for j in range(len(elements)):
                if result[i] == elements[j][key]:
                    result2.append(elements[j])
        print(result2)
    except IndexError:
        print("> Type valid key")


bubble_sort(elements, key='transaction_amount')
