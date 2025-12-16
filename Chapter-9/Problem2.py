def game():
    return 10


score = game()

file = open("./Hi-Score.txt", "rt")

content = file.read()


if content:
    hi_score = int(content)
else:
    hi_score = 0

if score > hi_score:
    with open("./Hi-Score.txt", "w") as f:
        f.write(str(score))
        print(f"New Score is {score}")
else:
    print(f"High score remain {score}")
