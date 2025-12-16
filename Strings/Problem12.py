def ExtractNumericDigits(str):

    sum = 0

    for s in str:
        if s.isdigit():
            sum += int(s)

    if sum == 0:
        print("There is no String!")
    else:
        print(f"Sum : {sum}")


if __name__ == "__main__":
    str = input("Enter your string: ")
    ExtractNumericDigits(str)
