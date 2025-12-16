def loan_approval(age, income, credit_score):
    if age < 21 or age > 60:
        return "Loan Rejected ❌ (Age not eligible)"

    if income < 25000:
        return "Loan Rejected ❌ (Income too low)"

    if credit_score >= 750:
        return "Loan Approved ✅"

    elif credit_score >= 650:
        return "Loan Approved with Conditions ⚠️"

    else:
        return "Loan Rejected ❌ (Low credit score)"


if __name__ == "__main__":
    age = int(input("Enter Your Age : "))
    income = int(input("Enter Your Income : "))
    credit_score = int(input("Enter Your credit score : "))

    print(loan_approval(age, income, credit_score))
