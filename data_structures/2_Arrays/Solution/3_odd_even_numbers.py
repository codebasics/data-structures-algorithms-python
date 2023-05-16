# max = int(input("Enter max number: "))

# odd_numbers = []

# for i in range(1, max):
#     if i % 2 == 1:
#         odd_numbers.append(i)

# print("Odd numbers: ", odd_numbers)

max = int(input("Enter max number: "))

odd_numbers = []
count = 1

for i in range(max/2):
    odd_numbers.append(count)
    count += 2

print("Odd numbers: ", odd_numbers)