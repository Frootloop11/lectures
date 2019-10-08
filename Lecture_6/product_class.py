# INDEX_ON_SALE = 2
#
#
# class Product:
#     def __init__(self, name="", price=0.0, is_on_sale=False):
#         print("Running init")
#         self.name = name
#         self.price = price
#         self.is_on_sale = is_on_sale
#
#     def __str__(self):
#         print("Running str")
#         return "{} ${:.2f} {}".format(self.name, self.price, self.is_on_sale)
#
#     def __repr__(self):
#         return str(self)
#
#     def on_sale(self):
#         on_sale_string = ""
#         if self.is_on_sale is True:
#             on_sale_string = "(On Sale!)"
#
#
# p = Product("Phone", 340)
# print(p)

products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
print(products)

on_sale_products = [product for product in products if product[2]]
print(on_sale_products)

# class Thing:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def change(self, b):
#         self.a += b
