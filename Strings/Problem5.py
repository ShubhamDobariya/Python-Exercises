def reverseStr(str):
    newStr = str[::-1]
    print(f"{str} reverse is {newStr}")


if __name__ == "__main__":
    str = input("Enter Your string : ")
    reverseStr(str)
