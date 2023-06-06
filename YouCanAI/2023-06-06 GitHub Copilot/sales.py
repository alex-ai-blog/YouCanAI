# Tracks the sales from a tech store

class inventory:
    def __init__(self, name, price, quantity, sales):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.sales = sales

    def __str__(self):
        return "Name: " + self.name + "\nPrice: " + str(self.price) + "\nQuantity: " + str(self.quantity)

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getQuantity(self):
        return self.quantity

    def getSales(self):
        return self.sales
    
    def make_sale(self, quantity):
        self.quantity -= quantity
        self.sales += quantity

    def restock(self, quantity):
        self.quantity += quantity

def main():
    # Create the inventory
    inventory1 = inventory("Laptop", 500, 10, 0)
    inventory2 = inventory("Desktop", 1000, 5, 0)
    inventory3 = inventory("Tablet", 200, 20, 0)

    # Print the inventory
    print(inventory1)
    print(inventory2)
    print(inventory3)

    # Make a sale
    inventory1.make_sale(2)
    inventory2.make_sale(1)
    inventory3.make_sale(5)

    # Print the inventory
    print(inventory1)
    print(inventory2)
    print(inventory3)

    # Restock
    inventory1.restock(5)
    inventory2.restock(2)
    inventory3.restock(10)

    # Print the inventory
    print(inventory1)
    print(inventory2)
    print(inventory3)

if __name__ == "__main__":
    main()