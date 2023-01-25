#1. Let us say your expense for every month are listed below,
#	1. January -  2200
# 	2. February - 2350
#    3. March - 2600
#    4. April - 2130
#    5. May - 2190

#Create a list to store these monthly expenses and using that find out,

#    1. In Feb, how many dollars you spent extra compare to January?
#    2. Find out your total expense in first quarter (first three months) of the year.
#    3. Find out if you spent exactly 2000 dollars in any month
#    4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
#    5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this


#creating a list in Python
expenses={'January':2200,'February':2350,'March':2600,'April':2130,'May':2190}
#solution to Q1
exp_diff_Jan_Feb=expenses['February']-expenses['January']
print(exp_diff_Jan_Feb)

#solution to Q2
tot_3=expenses['January']+expenses['February']+expenses['March']
print(tot_3)

#solution to Q3
def Q3(test_dict, amt):
    do_exist = False
    for key, val in test_dict.items():
        if val == amt:
            do_exist = True
    return do_exist
amt=2000
# Iterate over all key, value pairs in dict and check if value exist
if Q3(expenses, amt):
    print("True")
else:
    print("Not found")

#solution to Q4
expenses.update({'June':1980})
print(expenses)

#solution to Q5
expenses['April']=(expenses['April']-200)
print(expenses['April'])