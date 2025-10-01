class Order:
    all = []
    def __init__(self,customer,coffee,price):
        if not isinstance(price,float):
            raise Exception("Price must be a float")
        if not (1.0<= price <= 10.0):
            raise Exception("Price must be between 1.0 and 10.0")
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer
    @property
    def coffee(self):
        return self._coffee
    @property
    def price(self):
        return self._price