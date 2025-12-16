def sumNaturalNum(n):
    if n == 1:
        return 1

    return n + sumNaturalNum(n - 1)


if __name__ == "__main__":
    n = int(input("Enter natural number : "))

    print("sum is", sumNaturalNum(n))
