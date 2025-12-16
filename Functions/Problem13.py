def findMinMaxAvg(list):
    min = list[0]
    max = list[0]
    total = 0

    for num in list:
        if num < min:
            min = num

        if num > max:
            max = num

        total += num

    avg = total / 2

    print(f"Min Num = {min} || Max Num = {max} || Avg Num = {avg}")


if __name__ == "__main__":
    list = [11, 24, 53, 76, 54, 34, 28, 98]

    findMinMaxAvg(list)
