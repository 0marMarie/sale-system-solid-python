# Author     :  Omar Hamed Marie
# Description:  sale-system-improved-design-interface-segregation
# Date       :  10 SEP 2022
# Version    :  V 1.4


## Design Problem:
## Classes should depend on abstractions not concrete classes

## Solved Using:
## Dependency Inversion


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
    def pay(self, order):
        """
        Declaration of an abstract method to be initialized later
        Benefits: We can extend code by adding more subclasses without modifying PaymentMethods.
        
        @param order: this is the order object
        """
        pass


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self):
        pass


class SmsAuthorizer(Authorizer):
    """Inteface segregation refactor using composition"""
    authorized = False

    def auth_sms(self, code):
        print(f"Verfying sms code: {code}")
        self.authorized = True
    
    def is_authorized(self):
        return self.authorized


class RobotAuthorizer(Authorizer):
    """Inteface segregation refactor using composition"""
    authorized = False

    def auth_robot(self):
        print(f"Not a Robot")
        self.authorized = True
    
    def is_authorized(self):
        return self.authorized


class DebitPayment(PaymentMethods):
    
    def __init__(self, security_code, authorized: Authorizer):
        self.security_code = security_code
        self.authorized = authorized

    def pay(self, order):
        """Impementing the abstract method declared in PaymentMethod"""
        if not self.authorized.is_authorized():
            raise Exception("Not authorized.")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class CreditPayment(PaymentMethods):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        """Impementing the abstract method declared in PaymentMethod"""
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaybalPayment(PaymentMethods):

    def __init__(self, email_address, authorized: Authorizer):
        self.email_address = email_address
        self.authorized = authorized

    def pay(self, order):
        """Impementing the abstract method declared in PaymentMethod"""
        if not self.authorized.is_authorized():
            raise Exception("Not authorized.")
        print("Processing paybal payment type")
        print(f"Verifying email address: {self.email_address}")
        order.status = "paid"


## User code
order = Order()
order.add_item("Mouse", 1, 20)
order.add_item("Keyboard", 1, 100)
order.add_item("SSD", 1, 200)
order.add_item("USB cable", 2, 10)
print(order.total_price())

## Notes: Authorizer is not supported for credit payment method
##        Types of Authorization are RobotAuthorizer and SmsAuthorizer
authorizer = RobotAuthorizer()
processor = DebitPayment("2349875", authorizer)
authorizer.auth_robot()
processor.pay(order)