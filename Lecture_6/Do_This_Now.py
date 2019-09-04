INDEX_ON_SALE = 2

products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]

print(products)
on_sale_products = [product[0] for product in products if product[INDEX_ON_SALE]]
print(on_sale_products)



