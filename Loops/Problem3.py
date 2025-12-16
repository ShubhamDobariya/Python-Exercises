def SumOfNaturalNum(n):
    sum = 0

    for i in range(1, n + 1):
        sum += i

    print(f"Sum of {n} natural number is {sum}")


if __name__ == "__main__":
    n = int(input("Enter Natural Number : "))
    SumOfNaturalNum(n)
