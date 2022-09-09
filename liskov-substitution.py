# Author     :  Omar Hamed Marie
# Description:  sale-system-improved-design-liskov-substitution
# Date       :  9 SEP 2022
# Version    :  V 1.2


## Design Problem:
## If we added a new payment method we will need to modify the paymentMethod class

## Solved Using:
## Open Closed Principle

from abc import ABC, abstractmethod

class Order:
    
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        """Adding Items"""
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        """Computing the Total Price"""
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


# Create a new Pay class to separate payment from Order class
class PaymentMethods(ABC):
    """
    Abstract class to solve the violation of open closed principle

    Benefits: After separation order has one responsipility and pay has one responsipility
              Increased Cohesion
    drawback: Introduced some coupling
    """
    @abstractmethod
    def pay(self, order, security_code):
        """
        Declaration of an abstract method to be initialized later
        Benefits: We can extend code by adding more subclasses without modifying PaymentMethods.
        
        @param order: this is the order object
        @param security_code: this is the security code for product
        """
        pass


class DebitPayment(PaymentMethods):
    def pay(self, order, security_code):
        """Impementing the abstract method declared in PaymentMethod"""
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class CreditPayment(PaymentMethods):
    def pay(self, order, security_code):
        """Impementing the abstract method declared in PaymentMethod"""
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class PaybalPayment(PaymentMethods):
    def pay(self, order, security_code):
        """Impementing the abstract method declared in PaymentMethod"""
        print("Processing paybal payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


## User code
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = PaybalPayment()
processor.pay(order, "0372846")