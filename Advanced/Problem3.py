students = [("Shubham", 88), ("Parth", 72), ("Harsh", 95), ("Pujan", 70), ("DK", 65)]


students_sorted = sorted(students, key=lambda x: x[1])
students_sorted_descending = sorted(students, key=lambda x: x[1], reverse=True)

print("Ascending :", students_sorted)
print("Descending :", students_sorted_descending)
