from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Alice")
c2 = Customer("Bob")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

order1 = Order(c1, coffee1, 4.5)
order2 = Order(c2, coffee2, 3.0)

c1.create_order(coffee1, 4.5)
c1.create_order(coffee2, 3.0)
c2.create_order(coffee1, 5.0)

import pdb; pdb.set_trace()  # Debugging 