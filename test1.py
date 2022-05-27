numbers = []
input_number = input("Enter your Numbers: ")
data = 0
for i in range(len(input_number)):
    if i % 2 == 0:
        data = input_number[i]
    else:
        numbers.append(input_number[i])
        numbers.append(data)

if len(input_number) % 2 != 0:
    numbers.append(input_number[-1])

for i in numbers:
    print(i, end="")