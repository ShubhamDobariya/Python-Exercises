def palindrome(str):
    newStr = str[::-1]

    if newStr == str:
        print("Yes, string is palindrome")
    else:
        print("No, string is not palindrome")


if __name__ == "__main__":
    str = input("Enter Your string : ")
    palindrome(str)
