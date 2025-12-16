try:
    num1 = int(input("Enter Number 1 : "))
    num2 = int(input("Enter Number 2 : "))

    divide = num1 / num2

    print(divide)

except ZeroDivisionError as e:
    print(e)

except ValueError as e:
    print(e)
