def Pattern(n):

    for i in range(n):
        for j in range(i + 1):
            print("*", end="")

        for j in range(2 * (n - i - 1)):
            print(" ", end="")

        for j in range(i + 1):
            print("*", end="")

        print("")

    for i in range(n):
        for j in range(n, i, -1):
            print("*", end="")

        for j in range(n, (n - i), -1):
            print(2 * " ", end="")

        for j in range(n, i, -1):
            print("*", end="")

        print("")


if __name__ == "__main__":
    n = int(input("Enter number : "))
    Pattern(n)
