def removeDuplicate(lists):
    seen = set()

    for num in lists:
        if num not in seen:
            seen.add(num)

    return list(seen)


if __name__ == "__main__":
    lists = [1, 2, 5, 3, 2, 1, 3, 8, 4, 2, 10, 21, 11]

    print(removeDuplicate(lists))
