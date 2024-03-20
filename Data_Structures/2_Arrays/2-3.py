# 3. Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from a user using input() function

odd_numbers_list = []

max_number = int(input('What is the max number? '))

for i in range(0,max_number+1):
    if i%2 != 0:
        odd_numbers_list.append(i)

print(odd_numbers_list)

