def CountFreqOfNum(lists, num):
    count = 0

    for n in lists:
        if n == num:
            count += 1

    return count


if __name__ == "__main__":
    lists = [12, 45, 76, 56, 90, 66, 45, 90, 89, 67, 55, 23, 45, 90, 34, 34]
    num = 90
    print(CountFreqOfNum(lists, num))
