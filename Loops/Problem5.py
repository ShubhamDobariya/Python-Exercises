def CountNumOfDigit(n):
    numberofdigit = 0

    while n > 0:
        n //= 10
        numberofdigit += 1

    print(f"Total digit is {numberofdigit}")


if __name__ == "__main__":
    n = int(input("Enter Digit : "))
    CountNumOfDigit(n)
