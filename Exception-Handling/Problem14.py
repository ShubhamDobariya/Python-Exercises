while True:
    try:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))

        result = num1 / num2
        print("Result: ", result)

    except ValueError as e:
        print("Invalid input!", e)

    except ZeroDivisionError as e:
        print("Error:", e)

    except Exception as e:
        print("Unexpected error:", e)

    else:
        print("Calculation successful.")

    finally:
        print("Loop continues...\n")

    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() != "y":
        break
