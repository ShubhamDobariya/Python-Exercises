latter = """
    Dear <|Name|>,
    You are selected!
    <|Date|>
"""

print(latter.replace("<|Name|>", "shubham").replace("<|Date|>", "1 Jan 2026"))
