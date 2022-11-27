max = int(input("Enter max number: "))

odd_numbers = []

for i in range(1, max):
    if i % 2 == 1:              # or i % 2 != 0:
        odd_numbers.append(i)

print("Odd numbers: ", odd_numbers)
