try:
    file = open("./test.txt", "r")
    content = file.read()

except FileNotFoundError as e:
    print(e)
