def CircleArea(r, pi=3.14):
    r2 = r**2
    print(f"Circle Area is {pi*r2}")


if __name__ == "__main__":
    r = int(input("Enter circle radius : "))

    CircleArea(r)
