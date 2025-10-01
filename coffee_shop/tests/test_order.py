import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_create_order_valid():
    cust = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(cust, coffee, 4.5)
    assert order.customer == cust
    assert order.coffee == coffee
    assert order.price == 4.5
    assert order in Order.all

def test_price_validation_type():
    cust = Customer("Bob")
    coffee = Coffee("Mocha")
    ## Test with non-float price
    with pytest.raises(Exception):
        Order(cust, coffee, "5.0")  

def test_price_validation_bounds():
    cust = Customer("Charlie")
    coffee = Coffee("Cappuccino")
    with pytest.raises(Exception):
        Order(cust, coffee, 0.5) 
    ## Test with price below minimum 
    with pytest.raises(Exception):
        Order(cust, coffee, 15.0)  
