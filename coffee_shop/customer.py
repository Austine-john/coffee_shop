class Customer:
    all = []
    def __init__(self,name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if not isinstance(value,str) and 1<= (value) <=15:
            self._name = value
        else:
            raise Exception("Name must be a string between 1 and 15 characters")

