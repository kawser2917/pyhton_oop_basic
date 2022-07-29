class Item:
    
    def __init__(self,name,price,quantity):

        assert price>=0, f'price can not be less than zero'
        self.name=name
        self.price=price
        self.quantity=quantity
    def show(self):
        return f'{self.name}  {self.price} {self.quantity}'
    
    def calculated_total_price(self):
        return f'Total price = {self.price*self.quantity}'

item1=Item("Phone",0,5)
item2=Item("laptop",3000,10)

print(item1.show())
print(item2.show())
print()
print("--------------")
print()
print(item1.calculated_total_price())
print(item2.calculated_total_price())