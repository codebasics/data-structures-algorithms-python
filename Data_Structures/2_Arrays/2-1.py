# # Exercise: Array DataStructure

# 1. Let us say your expense for every month are listed below,
# 	1. January -  2200
#  	2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190

# Create a list to store these monthly expenses and using that find out,

#     1. In Feb, how many dollars you spent extra compare to January?
#     2. Find out your total expense in first quarter (first three months) of the year.
#     3. Find out if you spent exactly 2000 dollars in any month
#     4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#     5. You returned an item that you bought in a month of April and
#     got a refund of 200$. Make a correction to your monthly expense list
#     based on this

expenses = [2200,2350,2600,2130,2190]

# 1. In Feb, how many dollars you spent extra compare to January?

extraSpend = expenses[1] - expenses[0]

print(f"In February, you spent ${extraSpend} more than in January")

# 2. Find out your total expense in first quarter (first three months) of the year.

q1_expenses = sum(expenses[0:3])

print(f"In Q1, you spent ${q1_expenses}")

# 3. Find out if you spent exactly 2000 dollars in any month

print("Did I spent 2000$ in any month? ", 2000 in expenses) # False

did_i_spend = False

for e in expenses:
    if e == 2000:
        did_i_spend = True

if did_i_spend == True:
    print('You did spend exactly 2000 in a month')
else:
    print('You did not spend exactly 2000 in a month')

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    
expenses.append(1980)

print(expenses)

#  5. You returned an item that you bought in a month of April and
# #     got a refund of 200$. Make a correction to your monthly expense list
# #     based on this

expenses[3] = expenses[3] - 200
print(expenses)
