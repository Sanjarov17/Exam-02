count=("salom salom dunyo")
def count_words(text: str) -> dict:
    words = text.lower().split()
    result = {}
    for x in words:
        result[x] = result.get(x, 0) + 1
    return result
print(count_words(count))
