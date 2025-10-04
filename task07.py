cart = {
  'non': {'price': 3000, 'quantity': 2},
  'sut': {'price': 8000, 'quantity': 1},
  'olma': {'price': 5000, 'quantity': 5}
}
def calculate_cart(cart: dict) -> int:
    return sum(item["price"] * item["quantity"] for item in cart.values())

print(calculate_cart(cart))
