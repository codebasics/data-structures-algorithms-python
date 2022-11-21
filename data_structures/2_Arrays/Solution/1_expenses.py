# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#   3. March - 2600
#   4. April - 2130
#   5. May - 2190

def array_ex(arr, key, key1):
    # first question
    compare = int(arr[1][key]) - int(arr[0][key])
    print("1. In Feb, how many dollars you spent extra compare to January? : ", compare)

    # second question
    first_quarter = int(arr[0][key]) + int(arr[1][key]) + int(arr[2][key])
    print("2. Find out your total expense in first quarter (first three months) of the year. : ", first_quarter)

    # third question
    value = 0
    for i in range(len(arr)):
        if arr[i][key] == "2130":
            value += 1
        i += 1
    if value == 1:
        print("3. Find out if you spent exactly 2130 dollars in any month : ", value, "time")
    elif value > 1:
        print("3. Find out if you spent exactly 2130 dollars in any month : ", value, "times")
    else:
        print("3. Find out if you spent exactly 2130 dollars in any month : Zero")

    # fifth question
    refund = 0
    for i in range(len(arr)):
        if arr[i][key1] == "April":
            refund = int(arr[i][key]) - 200
        i += 1
    print("5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this : ", refund)

    # fourth question
    item_expense = [{'Month': 'June', 'E_Amount': '1980'}]
    arr.append(item_expense)
    print("4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list : ",
          arr)


if __name__ == '__main__':
    expense = [
        {'Month': 'January', 'E_Amount': '2200'},
        {'Month': 'February', 'E_Amount': '2350'},
        {'Month': 'March', 'E_Amount': '2600'},
        {'Month': 'April', 'E_Amount': '2130'},
        {'Month': 'May', 'E_Amount': '2190'}
    ]

    array_ex(expense, key="E_Amount", key1="Month")

exp[3] = exp[3] - 200
print("Expenses after 200$ return in April:",exp) # [2200, 2350, 2600, 1930, 2190, 1980]
