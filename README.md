# Exam 02

---

## **Masala 1: Calculator (Kalkulyator)**

**Funksiya**: `calculate(num1: float, num2: float, operator: str) -> float`

**Talab**: 
- 4 ta asosiy amal: `+`, `-`, `*`, `/`
- Nolga bo'lish xatosini ushlab qoling
- Noto'g'ri operator kiritilsa xato qaytaring
- Natijani 2 kasr xonagacha yaxlitlang

**Test case**:
```python
calculate(15, 3, "/")    # 5.0
calculate(8, 5, "*")     # 40.0
calculate(10, 0, "/")    # Error: Nolga bo'lish mumkin emas
calculate(7, 4, "^")     # Error: Noto'g'ri operator
```

---

## **Masala 2: Simple ATM Simulation**

**Funksiya**: `atm_operation(balance: int, action: str, amount: int) -> dict`

**Talab**:
- 3 ta amal: `deposit`, `withdraw`
- Withdraw uchun balans yetarli emasligini tekshiring
- Manfiy summa kiritsa xato qaytaring
- Natija: `balance`

**Test case**:
```python
atm_operation(100000, "deposit", 50000) # 150000

atm_operation(100000, "withdraw", 20000) # 80000
```

---

## **Masala 3: Tax Calculator (Soliq Kalkulyatori)**

**Funksiya**: `calculate_tax(salary: int) -> dict`

**Soliq me'yorlari**:
- 0 - 5,000,000: 0%
- 5,000,001 - 10,000,000: 12%
- 10,000,001 - 20,000,000: 18%
- 20,000,001+: 25%

**Talab**: 
- Natija: `{"gross": int, "tax": int, "net": int, "rate": str}`

**Test case**:
```python
calculate_tax(8_000_000)
# {"gross": 8000000, "tax": 360000, "net": 7640000, "rate": "12%"}

calculate_tax(3_000_000)
# {"gross": 3000000, "tax": 0, "net": 3000000, "rate": "0%"}
```

---

## **Masala 4: FISH Tartibini O'zgartirish**

**Funksiya**: `format_name(full_name: str) -> str`

**Talab**:
- FISH (Familiya Ism Sharif) formatini `Ism Sharif, Familiya` shaklida qaytaring

**Test case**:
```python
format_name("Aliyev Vali G'aniyevich")
# "Vali G'aniyevich, Aliyev"
```

---

## **Masala 5: So'zlar Sonini Hisoblash**

**Funksiya**: `count_words(text: str) -> dict`

**Talab**:
- Matn ichidagi har bir so'z necha marta qatnashganini aniqlang
- Katta-kichik harfni e'tiborga olmang

**Test case**:
```python
count_words("salom salom dunyo")
# {"salom": 2, "dunyo": 1}

count_words("Python python PYTHON")
# {"python": 3}
```

---

## **Masala 6: Baholar Tizimi**

**Funksiya**: `analyze_grades(students: dict) -> dict`

**Talab**:
- O'rtacha bahoni hisoblang
- O'rtachadan yuqori baho olganlarni aniqlang
- Natija: `{"average": float, "above_average": list}`

**Test case**:
```python
analyze_grades({"Ali": 5, "Vali": 4, "Hasan": 5, "Husan": 3})
# {"average": 4.25, "above_average": ["Ali", "Hasan"]}

analyze_grades({"Aziz": 3, "Bobur": 4, "Diyor": 5})
# {"average": 4.0, "above_average": ["Diyor"]}
```

---

## **Masala 7: Mahsulotlar Savatchasi**

**Funksiya**: `calculate_cart(cart: dict) -> int`

**Talab**:
- Har bir mahsulot uchun: narx × miqdor
- Umumiy summani hisoblang

**Test case**:
```python
cart = {
  'non': {'price': 3000, 'quantity': 2},
  'sut': {'price': 8000, 'quantity': 1},
  'olma': {'price': 5000, 'quantity': 5}
}
calculate_cart(cart)  # 37000
```

---

## **Masala 8: Yig'indi va O'rtacha**

**Funksiya**: `calculate_stats(numbers: list) -> dict`

**Talab**:
- Ro'yxatdagi sonlar yig'indisi
- O'rtacha qiymatni hisoblang
- Natija: `{"sum": int, "average": float}`

**Test case**:
```python
calculate_stats([3, 7, 10, -5, -8, 15, 22])
# {"sum": 44, "average": 6.29}

calculate_stats([10, 20, 30])
# {"sum": 60, "average": 20.0}
```

---

## **Masala 9: Eng Katta va Eng Kichik Son**

**Funksiya**: `find_min_max(numbers: list) -> dict`

**Talab**:
- Ro'yxatdagi eng katta sonni toping
- Ro'yxatdagi eng kichik sonni toping
- Natija: `{"max": int, "min": int}`

**Test case**:
```python
find_min_max([3, 7, 10, -5, -8, 15, 22])
# {"max": 22, "min": -8}

find_min_max([100, 50, 200, -10])
# {"max": 200, "min": -10}
```

---

## **Masala 10: Tartiblash**

**Funksiya**: `sort_numbers(numbers: list, reverse: bool = False) -> list`

**Talab**:
- Ro'yxatdagi sonlarni tartiblang
- `reverse=True` bo'lsa kamayish tartibida
- `reverse=False` bo'lsa o'sish tartibida

**Test case**:
```python
sort_numbers([3, 7, 10, -5, -8, 15, 22, 0])
# [-8, -5, 0, 3, 7, 10, 15, 22]

sort_numbers([3, 7, 10, -5], reverse=True)
# [10, 7, 3, -5]
```

---

## **Masala 11: List Operations**

**Funksiya**: `analyze_list(items: list) -> dict`

**Talab**:
- Jami elementlar soni
- Noyob elementlar soni
- Dublikat elementlar ro'yxati
- Eng ko'p takrorlangan element

**Test case**:
```python
analyze_list(["Ali", "Vali", "Ali", 1, 2, 1])
# {
#   "total": 6,
#   "unique": 4,
#   "duplicates": ["Ali", 1],
#   "most_common": "Ali"
# }
```

---

## **Masala 12: Ismlarni Alfavit Bo'yicha Tartiblash**

**Funksiya**: `sort_names(students: list) -> list`

**Talab**:
- Ismlar ro'yxatini alfavit bo'yicha tartiblang
- Katta-kichik harfni e'tiborga olmang

**Test case**:
```python
sort_names(["Ali", "Vali", "Hasan", "Husan", "Aziza"])
# ["Ali", "Aziza", "Hasan", "Husan", "Vali"]

sort_names(["Zara", "Bobur", "Anvar"])
# ["Anvar", "Bobur", "Zara"]
```

---

## **Masala 13: Uzun Ismlar**

**Funksiya**: `filter_long_names(students: list, min_length: int = 5) -> list`

**Talab**:
- Uzunligi `min_length` dan katta bo'lgan ismlarni ajrating

**Test case**:
```python
filter_long_names(["Ali", "Vali", "Hasan", "Husan", "Aziza", "Jasurbek"])
# ["Hasan", "Husan", "Aziza", "Jasurbek"]

filter_long_names(["Ali", "Muhammad", "Jo"], 4)
# ["Muhammad"]
```

---

## **Masala 14: Pattern Matching**

**Funksiya**: `find_pattern(items: list, pattern: str, match_type: str) -> list`

**Match turlari**:
- `"starts"`: Pattern bilan boshlanadi
- `"ends"`: Pattern bilan tugaydi
- `"contains"`: Pattern ichida bor

**Talab**:
- Case-insensitive bo'lsin

**Test case**:
```python
find_pattern(["Ali", "Alisher", "Vali", "Aziz"], "A", "starts")
# ["Ali", "Alisher", "Aziz"]

find_pattern(["Alisher", "Bobur", "Jasur"], "ur", "ends")
# ["Bobur", "Jasur"]

find_pattern(["Python", "Java", "JavaScript"], "java", "contains")
# ["Java", "JavaScript"]
```

---

## **Masala 15: Eng Yuqori Baho**

**Funksiya**: `find_top_students(grades: dict) -> dict`

**Talab**:
- Eng yuqori bahoni toping
- Shu bahoga ega bo'lgan barcha talabalarni qaytaring
- Natija: `{"max_grade": int, "students": list}`

**Test case**:
```python
find_top_students({"Ali": 5, "Vali": 4, "Hasan": 3, "Husan": 5})
# {"max_grade": 5, "students": ["Ali", "Husan"]}

find_top_students({"Aziz": 4, "Bobur": 5, "Diyor": 3})
# {"max_grade": 5, "students": ["Bobur"]}
```

---

## **Masala 16: Bahosi Bo'yicha Sanash**

**Funksiya**: `count_by_grade(grades: dict, target_grade: int) -> dict`

**Talab**:
- Ma'lum bahoga ega talabalar sonini hisoblang
- Ularning ismlarini qaytaring
- Natija: `{"count": int, "students": list}`

**Test case**:
```python
count_by_grade({"Ali": 5, "Vali": 4, "Hasan": 3, "Husan": 5}, 5)
# {"count": 2, "students": ["Ali", "Husan"]}

count_by_grade({"Aziz": 4, "Bobur": 4, "Diyor": 3}, 4)
# {"count": 2, "students": ["Aziz", "Bobur"]}
```

---

## **Masala 17: Musbat Sonlarni Ajratish**

**Funksiya**: `filter_positive(numbers: list) -> list`

**Talab**:
- Dict ichidagi `value` kaliti musbat bo'lgan elementlarni ajrating
- Asl strukturani saqlang

**Test case**:
```python
filter_positive([{'value': -5}, {'value': 10}, {'value': -1}, {'value': 7}])
# [{'value': 10}, {'value': 7}]

filter_positive([{'value': 0}, {'value': 5}, {'value': -3}])
# [{'value': 5}]
```

---

## **Masala 18: Sonlarni Kvadratga Oshirish**

**Funksiya**: `square_values(numbers: list) -> list`

**Talab**:
- Har bir dict ichidagi `value` ni kvadratga oshiring
- Yangi list qaytaring (asl list o'zgarmaydi)

**Test case**:
```python
square_values([{'value': 2}, {'value': 3}, {'value': 4}])
# [{'value': 4}, {'value': 9}, {'value': 16}]

square_values([{'value': -2}, {'value': 5}])
# [{'value': 4}, {'value': 25}]
```

---

## **Masala 19: Eng Uzun Ism**

**Funksiya**: `find_longest_name(names: list) -> str`

**Talab**:
- Ismlar ro'yxatidan eng uzunini toping
- Agar bir nechta bo'lsa, birinchisini qaytaring

**Test case**:
```python
find_longest_name(['Ali', 'Diyor', 'Jasurbek', 'Muhammad'])
# "Jasurbek"

find_longest_name(['Bo', 'Ali', 'Zara'])
# "Zara"
```

---

## **Masala 20: Eng Qisqa Ismli O'quvchi**

**Funksiya**: `find_shortest_name_student(students: list) -> str`

**Talab**:
- Dict'lar ro'yxatidan ismi eng qisqa bo'lgan o'quvchini toping
- Faqat ismni qaytaring
- Agar bir nechta bo'lsa, birinchisini qaytaring

**Test case**:
```python
students = [
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Ali', 'age': 18},
    {'name': 'Muhammad', 'age': 21}
]
find_shortest_name_student(students)  # {'name': 'Ali', 'age': 18}

students2 = [
    {'name': 'Jo', 'age': 19},
    {'name': 'Ali', 'age': 20},
    {'name': 'Bob', 'age': 18}
]
find_shortest_name_student(students2)  # {'name': 'Jo', 'age': 19}
```









# Exam 02 Solutions

# ---------------- Masala 1 ----------------
def calculate(num1: float, num2: float, operator: str) -> float:
    try:
        if operator == "+":
            return round(num1 + num2, 2)
        elif operator == "-":
            return round(num1 - num2, 2)
        elif operator == "*":
            return round(num1 * num2, 2)
        elif operator == "/":
            if num2 == 0:
                return "Error: Nolga bo'lish mumkin emas"
            return round(num1 / num2, 2)
        else:
            return "Error: Noto'g'ri operator"
    except Exception as e:
        return f"Error: {e}"


# ---------------- Masala 2 ----------------
def atm_operation(balance: int, action: str, amount: int) -> dict:
    if amount < 0:
        return {"error": "Manfiy summa kiritish mumkin emas"}
    if action == "deposit":
        balance += amount
    elif action == "withdraw":
        if amount > balance:
            return {"error": "Balans yetarli emas"}
        balance -= amount
    else:
        return {"error": "Noto‘g‘ri amal"}
    return {"balance": balance}


# ---------------- Masala 3 ----------------
def calculate_tax(salary: int) -> dict:
    if salary <= 5_000_000:
        rate = 0
    elif salary <= 10_000_000:
        rate = 12
    elif salary <= 20_000_000:
        rate = 18
    else:
        rate = 25
    tax = salary * rate // 100
    net = salary - tax
    return {"gross": salary, "tax": tax, "net": net, "rate": f"{rate}%"}


# ---------------- Masala 4 ----------------
def format_name(full_name: str) -> str:
    parts = full_name.split()
    family, rest = parts[0], " ".join(parts[1:])
    return f"{rest}, {family}"


# ---------------- Masala 5 ----------------
def count_words(text: str) -> dict:
    words = text.lower().split()
    result = {}
    for w in words:
        result[w] = result.get(w, 0) + 1
    return result


# ---------------- Masala 6 ----------------
def analyze_grades(students: dict) -> dict:
    avg = sum(students.values()) / len(students)
    above = [name for name, grade in students.items() if grade > avg]
    return {"average": round(avg, 2), "above_average": above}


# ---------------- Masala 7 ----------------
def calculate_cart(cart: dict) -> int:
    return sum(item["price"] * item["quantity"] for item in cart.values())


# ---------------- Masala 8 ----------------
def calculate_stats(numbers: list) -> dict:
    s = sum(numbers)
    avg = round(s / len(numbers), 2) if numbers else 0
    return {"sum": s, "average": avg}


# ---------------- Masala 9 ----------------
def find_min_max(numbers: list) -> dict:
    return {"max": max(numbers), "min": min(numbers)}


# ---------------- Masala 10 ----------------
def sort_numbers(numbers: list, reverse: bool = False) -> list:
    return sorted(numbers, reverse=reverse)


# ---------------- Masala 11 ----------------
from collections import Counter
def analyze_list(items: list) -> dict:
    total = len(items)
    counts = Counter(items)
    unique = len(counts)
    duplicates = [k for k, v in counts.items() if v > 1]
    most_common = counts.most_common(1)[0][0]
    return {
        "total": total,
        "unique": unique,
        "duplicates": duplicates,
        "most_common": most_common
    }


# ---------------- Masala 12 ----------------
def sort_names(students: list) -> list:
    return sorted(students, key=lambda x: x.lower())


# ---------------- Masala 13 ----------------
def filter_long_names(students: list, min_length: int = 5) -> list:
    return [name for name in students if len(name) >= min_length]


# ---------------- Masala 14 ----------------
def find_pattern(items: list, pattern: str, match_type: str) -> list:
    pattern = pattern.lower()
    result = []
    for item in items:
        low = item.lower()
        if match_type == "starts" and low.startswith(pattern):
            result.append(item)
        elif match_type == "ends" and low.endswith(pattern):
            result.append(item)
        elif match_type == "contains" and pattern in low:
            result.append(item)
    return result


# ---------------- Masala 15 ----------------
def find_top_students(grades: dict) -> dict:
    max_grade = max(grades.values())
    tops = [name for name, grade in grades.items() if grade == max_grade]
    return {"max_grade": max_grade, "students": tops}


# ---------------- Masala 16 ----------------
def count_by_grade(grades: dict, target_grade: int) -> dict:
    selected = [name for name, grade in grades.items() if grade == target_grade]
    return {"count": len(selected), "students": selected}


# ---------------- Masala 17 ----------------
def filter_positive(numbers: list) -> list:
    return [d for d in numbers if d["value"] > 0]


# ---------------- Masala 18 ----------------
def square_values(numbers: list) -> list:
    return [{"value": d["value"] ** 2} for d in numbers]


# ---------------- Masala 19 ----------------
def find_longest_name(names: list) -> str:
    return max(names, key=len)


# ---------------- Masala 20 ----------------
def find_shortest_name_student(students: list) -> dict:
    return min(students, key=lambda s: len(s["name"]))
