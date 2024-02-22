## 1. Let us say your expense for every month are listed below ##
expenses = [2200, 2350, 2600, 2130, 2190]

#1.1. In Feb, how many dollars you spent extra compare to January?
extra_spending = expenses[1] - expenses[0]
print(extra_spending)

#1.2. Find out your total expense in first quarter (first three months) of the year.
q1_expenses = 0
for i in range(3):
    q1_expenses += expenses[i]
print(q1_expenses)

#1.3. Find out if you spent exactly 2000 dollars in any month
for i in expenses:
    if i == 2000:
        print('Yes i spent 2000')
print('I did not')

#1.4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.insert(len(expenses), 1980)
print(expenses)

#1.5. You returned an item that you bought in a month of April and 
#got a refund of 200$. Make a correction to your monthly expense list
#based on this
expenses[3] = expenses[3] - 200
print(expenses)


## 2. You have a list of your favourite marvel super heros. ##

heros=['spider man','thor','hulk','iron man','captain america']

#Using this find out,
    #2.1. Length of the list
print(len(heros))

    #2.2. Add 'black panther' at the end of this list
heros.insert(len(heros), 'black panther')    
print(heros)

    #2.3. You realize that you need to add 'black panther' after 'hulk',
       #so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')

heros=['spider man','thor','hulk','iron man','captain america','hulk']


for i in range(len(heros)-1, -1, -1): #have to iterate in reverse because as new element is added, len(list) changes but range(len(list)) is not updated
    if heros[i] == 'hulk':
        print(i)
        print('yes')
        heros.insert(i+1, 'black panther')
       
print(heros)

    #2.4. Now you don't like thor and hulk because they get angry easily :)
       #So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
       #Do that with one line of code.
heros = ['dr.strange' if hero == 'thor' or hero == 'hulk' else hero for hero in heros]
heros = ['dr.strange' if hero in ['thor', 'hulk'] else hero for hero in heros]
print(heros)      
    #2.5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
sorted_heros = sorted(heros)
print(sorted_heros)

## 3. Create a list of all odd numbers between 1 and a max number. ##
#Max number is something you need to take from a user using input() function
max_number = input('Enter a number: ')
odd_numbers = [num for num in range(1, int(max_number)+1) if num % 2 != 0]
print(odd_numbers)
