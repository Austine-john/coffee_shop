from order import Order
class Coffee:
    all = []
    def __init__(self,name):
        if isinstance(name,str) and len(name) >=3:  
            self.name = name
            Coffee.all.append(self)

        else:
            raise Exception("Name must be a string with at least 3 characters")
        
    @property
    def name(self):
        return self._name

    def orders(self):
        return[order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        return sum([order.price for order in orders])/len(orders) if orders else 0