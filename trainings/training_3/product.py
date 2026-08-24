class Product:
    def __init__(self, name, price):
        self.productName = name
        self.productPrice = price

    def getName(self):
        return self.productName

    def getPrice(self):
        return self.productPrice

    def aboutProduct(self):
        return f"Продукт: {self.productName}, Цена: {self.productPrice}"
