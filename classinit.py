class cars:
    def __init__(self,brand,price):
        self.name_price={brand:price} #create a dict
   
    def add_name(self,brand,price):
        self.name_price[brand] = price        
    def print_all(self):
        for brand,price in self.name_price.items():
            print(f"{brand} price is {price}")

p1=cars("swift",250000)
p1.add_name("FOrd",300000)
p1.add_name("duster",60000)
p1.print_all()