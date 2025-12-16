def Factorial(num):
    if num == 0 or num == 1:
        return 1

    return num * Factorial(num - 1)


if __name__ == "__main__":
    num = int(input("Enter Number : "))

    print(Factorial(num))
