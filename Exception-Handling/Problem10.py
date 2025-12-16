try:
    num1 = int(input("Enter number 1: "))

    try:
        num2 = int(input("Enter number 2: "))

        res = num1 / num2
        print("result", res)
    except ZeroDivisionError as e:
        print(e)

except ValueError as e:
    print(e)
