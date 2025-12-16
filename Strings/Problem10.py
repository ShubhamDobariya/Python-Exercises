import string


def RemoveSpecialChar(str):
    newStr = ""
    for s in str:
        if s not in string.punctuation:
            newStr += s

    print(f"New String is {newStr}")


if __name__ == "__main__":
    str = input("Enter your string: ")
    RemoveSpecialChar(str)
