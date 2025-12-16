def TakeMarkandMinMaxAvg(marks):
    min = marks[0]
    max = marks[0]

    total = 0

    for mark in marks:
        if mark > max:
            max = mark

        if mark < min:
            min = mark

        total += mark

    avg = total / len(marks)

    print(f"Max Mark '{max}' || Min Mark '{min}' || Avg mark '{avg}'")


if __name__ == "__main__":

    marks = list(map(int, input("Enter your marks : ").split()))

    TakeMarkandMinMaxAvg(marks)
