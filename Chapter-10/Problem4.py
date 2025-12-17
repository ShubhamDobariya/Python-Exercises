class Calculator:
    def __init__(self, num):
        self.num = num

    @staticmethod
    def greet():
        print("Hello! Welcome to the Calculator.")

    def square(self):
        print(f"Square of {self.num} is {self.num ** 2}")

    def cube(self):
        print(f"Cube of {self.num} is {self.num ** 3}")

    def squareRoot(self):
        print(f"Square root of {self.num} is {self.num ** 0.5}")


if __name__ == "__main__":
    Calculator.greet()
    num = int(input("Enter a number: "))
    c1 = Calculator(num)
    c1.square()
    c1.cube()
    c1.squareRoot()
