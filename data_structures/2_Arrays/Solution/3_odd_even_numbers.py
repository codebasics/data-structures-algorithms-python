max = int(input("Enter max number: "))

odd_numbers = []
even_numbers=[]

for i in range(max):
    if i%2 == 1:
        odd_numbers.append(i)
    else:
        even_numbers.append(i)

print("Odd numbers: ",odd_numbers)
print("Even numbers:",even_numbers)
