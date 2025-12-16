def PalindromeNum(n):
    num = n
    reverseNumber = 0

    while n > 0:
        last = n % 10
        reverseNumber = reverseNumber * 10 + last
        n //= 10

    if num == reverseNumber:
        print("Number is Palindrome Number")
    else:
        print("Number is not Palindrome Number")


if __name__ == "__main__":
    n = int(input("Enter number : "))
    PalindromeNum(n)
