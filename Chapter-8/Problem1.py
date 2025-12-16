def greatest(a, b, c):
    maxNum = a

    if b > maxNum:
        maxNum = b
    else:
        maxNum = c

    print(f"Max number is {maxNum}")


if __name__ == "__main__":
    a = 25
    b = 23
    c = 79

    greatest(a, b, c)
