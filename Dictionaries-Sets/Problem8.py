marks = {"shubham": 98, "pujan": 79, "parth": 89, "kishan": 60}


new = sorted(marks.items(), key=lambda x: x[1])

print(dict(new))
