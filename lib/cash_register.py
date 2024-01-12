# # #!/usr/bin/env python3
import ipdb
class CashRegister:
    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items=[]
        self.previous_transactions=[]

    def add_item(self, item, price, quantity = 1):
        self.total += price*quantity
        for i in range(quantity):
            self.items.append(item)
        self.previous_transactions.append(
            {'item': item, 'price': price, 'quantity': quantity}
        )
    
    def apply_discount(self):
        if self.discount:
            self.total = int(self.total*((100-self.discount)/100))
            print(f'After the discount, the total comes to ${self.total}.')
        else:
            print('There is no discount to apply.')
    def void_last_transaction(self):
        self.total -= self.previous_transactions[-1].get('price') * self.previous_transactions[-1].get('quantity')
        self.previous_transactions.pop()

new_register = CashRegister()
new_register.add_item("eggs", 1.99)
new_register.add_item("tomato", 1.76)
new_register.void_last_transaction()
print(new_register.total)





    



    

