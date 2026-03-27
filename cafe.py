class Coffee:
    def __init__(self, name, description, base_price):
        self.name = name        
        self.description = description
        self.base_price = base_price
        
    def __str__(self): 
        return f"{self.name}: {self.description} -${self.base_price:.2f}"

class Order:
    def __init__(self, coffee, size):
        self.coffee = coffee
        self.size = size
        self.price = self.calculate_price()
    def calculate_price(self):
        price = self.coffee.base_price
        if self.size== "Small":
            extra = 0
        elif self.size == "Medium":
            extra = 0.5
        elif self.size == "Large":
            extra = 1.0
        else:
            extra = 0
        return price + extra

    def __str__(self):
        return f"{self.size} {self.coffee.name} - ${self.price:.2f}"

class Cafe:
    def __init__(self, name, tax_rate=0.08):
        self.name = name
        self.menu = []
        self.orders = []
        self.tax_rate = tax_rate

    def add_to_menu(self, coffee):
        self.menu.append(coffee)
        
    def display_menu(self):
        print(f"\n=== {self.name.upper()} MENU ===")

        for i, coffee in enumerate(self.menu, start=1):
            print(f"{i}. {coffee}")

    def add_order(self ,coffee ,size):
        new_order = Order(coffee, size)
        self.orders.append(new_order)
        print(f"\nAdded new order: {new_order}")
    def calculate_total(self):
        total = 0
        for order in self.orders:
            total += order.price
        return total

cafe = Cafe("Arab Cafe")

# add drinks to menu
cafe.add_to_menu(Coffee("Espresso", "Strong and bold coffee", 4.0))
cafe.add_to_menu(Coffee("Latte", "Espresso with steamed milk", 6.0))
cafe.add_to_menu(Coffee("Cappuccino", "Espresso with steamed milk and foam", 6.5))
cafe.add_to_menu(Coffee("Americano", "Espresso with hot water", 4.5))

# display menu
cafe.display_menu()cd works\Hala

# add orders
cafe.add_order(cafe.menu[0], "Medium")
cafe.add_order(cafe.menu[1], "Large")
cafe.add_order(cafe.menu[2], "Small")

# calculate total
total = cafe.calculate_total()
print(f"\nTotal: ${total:.2f}")