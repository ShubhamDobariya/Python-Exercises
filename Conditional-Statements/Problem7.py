python = int(input("Enter Your Python Mark : "))
os = int(input("Enter Your OS Mark : "))
dbms = int(input("Enter Your DBMS Mark : "))


percentage = (python + os + dbms) / 300 * 100

if percentage > 90 and percentage < 100:
    print("Your Grade ia A")
elif percentage > 80:
    print("Your Grade ia B")
elif percentage > 70:
    print("Your Grade ia C")
elif percentage > 60:
    print("Your Grade ia D")
elif percentage > 50:
    print("Your Grade ia E")
else:
    print("Your fail")
