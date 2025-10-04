def format_name(full_name: str) -> str:
    parts = full_name.split()
    family, rest = parts[0], " ".join(parts[1:])
    return f"{rest}, {family}"
print(format_name("Toshmatov Anvar Bekzodovich"))