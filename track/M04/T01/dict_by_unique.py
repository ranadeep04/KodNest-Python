products = [
    {"code": "P101", "name": "Keyboard", "price": 1200},
    {"code": "P102", "name": "Mouse", "price": 600},
    {"code": "P103", "name": "Monitor", "price": 8500}
]

# Step 1: Build the indexed dictionary
product_by_code = {}

for product in products:
    code = product["code"]

    if code not in product_by_code:
        product_by_code[code] = product

print(product_by_code)