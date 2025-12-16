def FindMinMaxNum(lists):

    min = lists[0]
    max = lists[0]

    for num in lists:
        if num > max:
            max = num

        if num < min:
            min = num

    print(f"Min Num : {min} || Max Num : {max}")


if __name__ == "__main__":
    lists = [122, 54, 35, 57, 67, 54, 89, 67, 98, 654, 89]
    FindMinMaxNum(lists)
