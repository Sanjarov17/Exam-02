students = [
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Ali', 'age': 18},
    {'name': 'Muhammad', 'age': 21}
]
def find_shortest_name_student(students: list) -> dict:
    return min(students, key=lambda s: len(s["name"]))
print(find_shortest_name_student(students))