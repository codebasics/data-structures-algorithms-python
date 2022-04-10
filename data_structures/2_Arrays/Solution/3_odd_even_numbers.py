max = int(input("Enter max number: "))

odd_numbers = []
#if number will be odd in that case it will omit the last number for that
if max % 2 == 0:
    max = max
else:
    max += 1
for i in range(1, max):
    if i % 2 == 1:
        odd_numbers.append(i)

print("Odd numbers: ", odd_numbers)
