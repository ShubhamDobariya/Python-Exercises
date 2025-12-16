def Factorial(n):
    ans = 1

    for i in range(2, n + 1):
        ans *= i

    print(f"Factorial Number is {ans}")


if __name__ == "__main__":
    n = int(input("Enter number : "))
    Factorial(n)
