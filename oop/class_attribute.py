class Item:
    pay_rate=0.8
    
    def __init__(self,name,price,quantity):

        assert price>=0, f'price can not be less than zero'
        self.name=name
        self.price=price
        self.quantity=quantity
    def show(self):
        return f'{self.name}  {self.price} {self.quantity}'
    
    def calculated_total_price(self):
        return f'Total price = {self.price*self.quantity}'
    
    def discount_price(self):
        return f"Discount price = {self.price*self.pay_rate}"

item1=Item("Phone",100,5)
item2=Item("laptop",3000,10)
item2.pay_rate=0.7

print(item1.show())
print(item2.show())
print()
print("--------------")
print()
print(item1.calculated_total_price())
print(item2.calculated_total_price())
print()
print("--------------")
print(item1.discount_price())
print(item2.discount_price())

print(Item.__dict__)
print(item1.__dict__)
print(item2.__dict__)