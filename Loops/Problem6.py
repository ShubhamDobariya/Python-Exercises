def reverseNum(n):
    num = n
    reverseNumber = 0

    while n > 0:
        last = n % 10
        reverseNumber = reverseNumber * 10 + last
        n //= 10

    print(f"{num} reverse number is {reverseNumber}")


if __name__ == "__main__":
    n = int(input("Enter number : "))
    reverseNum(n)
