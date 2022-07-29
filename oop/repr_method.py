class Item:
    pay_rate=0.8
    all=[]
    
    def __init__(self,name,price,quantity):

        assert price>=0, f'price can not be less than zero'
        self.name=name
        self.price=price
        self.quantity=quantity
        Item.all.append(self)
    def show(self):
        return f'{self.name}  {self.price} {self.quantity}'
    
    def calculated_total_price(self):
        return f'Total price = {self.price*self.quantity}'
    
    def discount_price(self):
        return f"Discount price = {self.price*self.pay_rate}"

    # def __repr__(self):
    #     return f"{self.name},{self.price},{self.quantity}"


item1=Item("Phone",100,5)
item2=Item("laptop",3000,10)

print(Item.all)