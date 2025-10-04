students = ["Ali", "Vali", "Hasan", "Husan", "Aziza", "Jasurbek"]

def filter_long_names(students: list, min_length: int = 5) -> list:
    return [name for name in students if len(name) >= min_length]

print(filter_long_names(students))
