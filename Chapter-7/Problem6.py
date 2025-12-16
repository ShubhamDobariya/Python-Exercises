def Factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return f"{n} factorial is {fact}"


if __name__ == "__main__":
    n = int(input("Enter Number! : "))

    print(Factorial(n))
