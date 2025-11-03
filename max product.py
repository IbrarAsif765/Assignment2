def max_product1(product1):
    max_price = float('-inf')
    max_product = ''
    for category, items in products.items():
        for product, price in items.items():
            if price > max_price:
                max_price = price
                max_product = product
    print(max_product, max_price)
product1 = {
    "Electronics": {"Laptop": 1200, "Phone": 800},
    "Clothes": {"Shirt": 50, "Shoes": 100}
}
max_product1(product1) 
