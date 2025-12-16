n = int(input("Enter natural number : "))

# using for loop
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)

# mathematically
sum = n * (n + 1) / 2
print(sum)

# using while loop
i = 1
sum = 0
while i <= n:
    sum += i
    i += 1

print(sum)
