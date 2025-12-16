unit = int(input("Enter your bill unit : "))

if unit <= 100:
    print(f"Your electricity bill is {unit*5}")
elif unit <= 200:
    print(f"Your electricity bill is {(100*5) + (unit - 100)*7 }")
else:
    print(f"Your electricity bill is {(100*5) + (100*7) + (unit - 200)*10}")
