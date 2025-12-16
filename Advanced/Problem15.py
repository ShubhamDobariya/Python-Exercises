from typing import List, Dict
from functools import reduce


def analyze_numbers(numbers: List[int]) -> Dict[str, float]:
    if not numbers:
        raise ValueError("numbers list can not be empty")

    analysis = {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "max": max(numbers),
        "min": min(numbers),
        "evenNum": list(filter(lambda x: x % 2 == 0, numbers)),
        "oddNum": list(filter(lambda x: x % 2 != 0, numbers)),
        "square": [num**2 for num in numbers],
        "product": reduce(lambda x, y: x * y, numbers),
    }

    return analysis


if __name__ == "__main__":
    try:
        while (data := input("Enter numbers: ")).strip():
            nums = list(map(int, data.split()))

            result = analyze_numbers(nums)

            for key, value in result.items():
                print(f"{key}: {value}")
            break

    except ValueError as e:
        print("Error: ", e)
