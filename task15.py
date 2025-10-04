tops = ({"Ali": 5, "Vali": 4, "Hasan": 3, "Husan": 5})
def find_top_students(grades: dict) -> dict:
    max_grade = max(grades.values())
    tops = [name for name, grade in grades.items() if grade == max_grade]
    return {"max_grade": max_grade, "students": tops}

print(find_top_students(tops))