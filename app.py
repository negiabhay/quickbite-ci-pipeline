def calculate_total(price, quantity):
    return price + quantity

def apply_discount(total, discount_percent):
    discount = (discount_percent / 100) * total
    return total - discount
