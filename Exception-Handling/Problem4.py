try:
    num1 = int(input("Enter Number 1 : "))
    num2 = int(input("Enter Number 2 : "))

    res = num1 / num2

except ZeroDivisionError as e:
    print(e)

else:
    print("Result", res)
