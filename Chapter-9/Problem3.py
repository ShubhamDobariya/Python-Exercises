for i in range(2, 20):
    file_name = f"tables/table_{i}.txt"
    with open(file_name, "w") as f:
        for j in range(1, 11):
            line = f"{i} X {j} = {i*j}\n"
            f.write(line)
