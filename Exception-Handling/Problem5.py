try:
    file = open("./test.txt", "r")
    content = file.read()

except FileNotFoundError as e:
    print(e)

finally:
    try:
        file.close()
        print("finally file closed!")
    except ValueError:
        print(ValueError)
