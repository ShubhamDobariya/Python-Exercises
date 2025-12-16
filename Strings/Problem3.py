def char(str, ch):
    isExists = False

    for s in str.lower():
        if s == ch.lower():
            isExists = True
            break

    if isExists:
        print("Yes, character exists in a given string.")
    else:
        print("No, character exists in a given string.")


if __name__ == "__main__":
    str = input("Enter Your string : ")
    ch = "d"
    char(str, ch)
