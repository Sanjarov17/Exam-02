analyze = {"Ali": 5, "Vali": 4, "Hasan": 5, "Husan": 3}

def analyze_grades(students: dict) -> dict:
    a = sum(students.values()) / len(students)
    baland = [name for name, grade in students.items() if grade > a]
    return {"average": a, "above_average": baland}

print(analyze_grades(analyze))
