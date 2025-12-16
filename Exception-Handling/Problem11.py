from datetime import datetime


def log_exception(error):
    with open("./error.log", "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {error}\n")


try:
    num1 = int(input("Enter Number 1 :"))
    num2 = int(input("Enter Number 2 :"))

    res = num1 / num2

    print("result", res)

except Exception as e:
    print("An error occurred! Logging error...")
    log_exception(e)

except ValueError as e:
    print("An error occurred! Logging error...")
    log_exception(e)
