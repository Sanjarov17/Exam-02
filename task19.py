name =(['Ali', 'Diyor', 'Jasurbek', 'Muhammad'])
def find_longest_name(names: list) -> str:
    return max(names, key=len)

print(find_longest_name(name))
