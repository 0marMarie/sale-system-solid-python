# Author     :  Omar Hamed Marie
# Description:  sale-system-improved-design-single-responsipility
# Date       :  8 SEP 2022
# Version    :  V 1.2


## Design Problem:
## Every class should only be responsible to one thing

## Solved Using:
## Single Responsibility Principle


from concurrent.futures import process


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
class paymentMethods:
    """
    Payment Methods class

    Benefits: After separation order has one responsipility and pay has one responsipility
              Increased Cohesion
    drawback: Introduced some coupling
    """
    def debit_type(self, order, security_code):
        """ 
        This is the debit type method.

        @param order: this is the order object
        @param security_code: this is the security code for product
        @return: None
        """
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

    def credit_type(self, order, security_code):
        """ 
        This is the credit type method.

        @param order: this is the order object
        @param security_code: this is the security code for product
        @return: None
        """
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


## User code
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = paymentMethods()
processor.credit_type(order, "0372846")