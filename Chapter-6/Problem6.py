sub1 = float(input("Enter sub 1 mark : "))
sub2 = float(input("Enter sub 2 mark : "))
sub3 = float(input("Enter sub 3 mark : "))

total = sub1 + sub2 + sub3

percentage = (total / 300) * 100


if percentage >= 90 and percentage <= 100:
    print(f"Your grade 'Ex' and percentage is {percentage:.2f}")
elif percentage >= 80:
    print(f"Your grade 'A' and percentage is {percentage:.2f}")
elif percentage >= 70:
    print(f"Your grade 'B' and percentage is {percentage:.2f}")
elif percentage >= 60:
    print(f"Your grade 'C' and percentage is {percentage:.2f}")
elif percentage >= 50:
    print(f"Your grade 'D' and percentage is {percentage:.2f}")
else:
    print(f"Your grade 'F' and percentage is {percentage:.2f}")
