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

result = calculate_tax(12_000_000)
print(result)
