try:
    with open("./Problem19.txt", "rt") as f:
        content = f.read()
        print(content)
except FileNotFoundError as e:
    print(e)
