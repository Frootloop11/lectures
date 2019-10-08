# from Lecture_6.product_class import Product
#
# MENU_STRING = "D.isplay products\nA.dd Products\nP.ut on Sale"
# FILENAME = "products.txt"
#
#
# def main():
#     products = load_products(FILENAME)
#     print(MENU_STRING)
#     choice = input("> ").upper()
#     while choice != "Q":
#         if choice == "D":
#             display_products(products)
#             print("D")
#         else:
#             print("Invalid")
#         print(MENU_STRING)
#         choice = input("> ").upper()
#
#
# def display_products():
#     for product in products:
#         print(product)
#
#
# def load_products():
#     products = []
#     with open(filename) as input_file:
#         for line in input_file:
#             # print(repr(line))
#             parts = line.strip().split(',')
#             # print(parts)
#             is_on_sale = parts[2] == "on"
#             product = Product(parts[0], float(parts[1]), is_on_sale)
#             products.append(product)
#     return products
#
#
# if __name__ =
