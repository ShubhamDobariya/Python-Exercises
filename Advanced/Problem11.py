from typing import List


def calculate_Sum(num: List[int]) -> int:
    return sum(num)


if __name__ == "__main__":
    num = [10, 20, 30, 40]

    print(calculate_Sum(num))
