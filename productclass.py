class Product:
    def __init__(self, Product_name: str, Price: int) -> None:
        self.Product_name = Product_name
        self.Price = Price

    def net_price(self):
        print("Net Price is inclusive of 12% Tax")
        print("Net Price:",self.Price + (self.Price*12//100))

    def base_price(self):
        print("Base Price:", self.Price)

    def set_price(self, Price=""):
        self.Price = Price

    def hike_price(self, per):
        self.Price = (self.Price + (self.Price*per//100))

    def details(self):
        print("Product:", self.Product_name)
        print("Price:", self.Price)


p1 = Product("Bottle", 100)
p1.net_price()
p1.base_price()
p1.set_price(2000)
p1.hike_price(15)
p1.details()
