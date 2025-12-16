numbers = []


for i in range(1, 5):
    num = int(input(f"Enter num {i} : "))
    numbers.append(num)


sum = sum(numbers)

print(sum)
