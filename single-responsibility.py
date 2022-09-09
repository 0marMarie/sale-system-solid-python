# Author     :  Omar Hamed Marie
# Description:  sale-system-improved-design-single-responsipility
# Date       :  8 SEP 2022
# Version    :  V 1.1


## Design Problem:
## Every class should only be responsible to one thing

## Solved Using:
## Single Responsibility Principle


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

    def pay(self, payment_type, security_code):
        """Paying the Order"""
        if payment_type == "debit":
            print("Processing debit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment type")
            print(f"Verifying security code: {security_code}")
            self.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")


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


order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
order.pay("debit", "0372846")