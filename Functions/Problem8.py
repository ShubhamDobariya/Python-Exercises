def CelsiusToFahrenheit(temp):
    print(f"{temp} Celsius is equal to {(temp * (9/5) + 32)} F")


if __name__ == "__main__":
    temp = float(input("Enter Temperature in  Celsius : "))

    CelsiusToFahrenheit(temp)
