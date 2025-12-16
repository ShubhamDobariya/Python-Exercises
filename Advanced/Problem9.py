def calculator():
    while True:
        print("\n===== Calculator Menu =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("Enter Your Choice(1-5): "))

        match choice:
            case 1:
                num1 = int(input("Enter first number : "))
                num2 = int(input("Enter second number : "))

                print(f"Addition of {num1} and {num2} is {num1+num2}")

            case 2:
                num1 = int(input("Enter first number : "))
                num2 = int(input("Enter second number : "))

                print(f"Subtraction of {num1} and {num2} is {num1-num2}")

            case 3:
                num1 = int(input("Enter first number : "))
                num2 = int(input("Enter second number : "))

                print(f"Multiplication of {num1} and {num2} is {num1*num2}")

            case 4:
                num1 = int(input("Enter first number : "))
                num2 = int(input("Enter second number : "))

                print(f"Division of {num1} and {num2} is {num1/num2}")

            case 5:
                print("Goodbye!")
                return

            case _:
                print("Invalid choice! Please select 1-5.")


if __name__ == "__main__":
    calculator()
