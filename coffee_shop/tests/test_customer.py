import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_create_customer():
    c = Customer("Alice")
    assert c.name == "Alice"
    assert c in Customer.all

def test_create_order_from_customer():
    cust = Customer("Bob")
    coffee = Coffee("Latte")
    order = cust.create_order(coffee, 5.0)
    assert order.customer == cust
    assert order.coffee == coffee
    assert order.price == 5.0

def test_customer_orders_and_coffees():
    cust = Customer("Charlie")
    coffee1 = Coffee("Mocha")
    coffee2 = Coffee("Cappuccino")
    Order(cust, coffee1, 4.5)
    Order(cust, coffee2, 5.0)
    assert set(cust.coffees()) == {coffee1, coffee2}
    assert len(cust.orders()) == 2

def test_customer_name_validation():
    ## Test with empty name and name longer than 15 characters
    with pytest.raises(Exception):
        Customer("") 
    with pytest.raises(Exception):
        Customer("A"*16)  
