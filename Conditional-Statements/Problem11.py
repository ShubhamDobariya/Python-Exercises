x = int(input("Enter x side : "))
y = int(input("Enter y side : "))
z = int(input("Enter z side : "))


if x == y == z:
    print("Equilateral triangle")
elif x == y or y == z or x == z:
    print("Isosceles triangle")
else:
    print("Scalene Triangle")
