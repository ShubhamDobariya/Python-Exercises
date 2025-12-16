lists = [10, 23, 55, 20, 34, 45, 65, 78, 98, 90, 100]

divisibleBy5 = list(filter(lambda x: x % 5 == 0, lists))


print(divisibleBy5)
