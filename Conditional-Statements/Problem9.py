num1 = int(input("Enter Number 1 : "))
op = input("Choice operation (+, -, *, /, % ) : ")
num2 = int(input("Enter Number 2 : "))


if op == "+":
    print(f"{num1} + {num2} = {num1+num2}")
elif op == "-":
    print(f"{num1} - {num2} = {num1-num2}")
elif op == "*":
    print(f"{num1} * {num2} = {num1*num2}")
elif op == "/":
    print(f"{num1} / {num2} = {num1/num2}")
elif op == "%":
    print(f"{num1} % {num2} = {num1%num2}")
else:
    print("Enter vaild operation from (+, -, *, /, % )")
