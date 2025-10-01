import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_create_coffee():
    c = Coffee("Latte")
    assert c.name == "Latte"
    assert c in Coffee.all

def test_orders_and_num_orders():
    coffee = Coffee("Mocha")
    cust = Customer("Alice")
    Order(cust, coffee, 4.5)
    Order(cust, coffee, 5.0)
    assert coffee.num_orders() == 2
    assert coffee.orders() == Order.all

def test_customers_method():
    coffee = Coffee("Cappuccino")
    cust1 = Customer("Bob")
    cust2 = Customer("Charlie")
    Order(cust1, coffee, 3.5)
    Order(cust2, coffee, 4.0)
    assert set(coffee.customers()) == {cust1, cust2}

def test_average_price():
    coffee = Coffee("Espresso")
    cust = Customer("Dave")
    Order(cust, coffee, 4.0)
    Order(cust, coffee, 6.0)
    assert coffee.average_price() == 5.0
