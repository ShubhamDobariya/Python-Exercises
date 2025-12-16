x = int(input("Enter x side : "))
y = int(input("Enter y side : "))
z = int(input("Enter z side : "))


if x > 0 and y > 0 and z > 0 and (x + y > z and y + z > x and x + z > y):
    print("It is Valid Triangle")
else:
    print("It is not Valid Triangle")
