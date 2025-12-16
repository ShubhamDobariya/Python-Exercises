num = int(input("Enter Number : "))

if num % 5 == 0 and num % 7 == 0:
    print(f"Yes, {num} is divisible by 5 and 7")
else:
    print(f"No, {num} is not divisible by 5 and 7")
