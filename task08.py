calculate=([10, 20, 30])

def calculate_stats(numbers: list) -> dict:
    s = sum(numbers)
    a = round(s / len(numbers), 2) if numbers else 1
    return {"sum": s, "average": a}

print(calculate_stats(calculate))