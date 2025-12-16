sub1 = float(input("Enter sub 1 mark : "))
sub2 = float(input("Enter sub 2 mark : "))
sub3 = float(input("Enter sub 3 mark : "))

total = sub1 + sub2 + sub3

percentage = (total / 300) * 100

if percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33:
    print(f"you passed and your persent is {percentage:.2f}")
else:
    print("you failed")
