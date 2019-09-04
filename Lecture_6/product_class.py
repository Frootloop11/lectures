INDEX_ON_SALE = 2


class Product:
    def __init__(self, name="", price=0.0, is_on_sale=False):
        print("Running init")
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        on_sale_string = ""
        if self.is_on_sale:
            on_sale_string = "(On Sale!)"
        print("Running str")
        return "{} ${:.2f} {}".format(self.name, self.price, self.is_on_sale)

    def __repr__(self):
        return str(self)


p = Product("Phone", 340)
print(p)

products = [Product("Phone", 340, False), Product("PC", 1420.95, True), Product("Plant", 24.5, True)]
