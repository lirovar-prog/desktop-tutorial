from abc import ABC, abstractmethod
class MenuItem(ABC):
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
    @abstractmethod
    def calculate_price(self):
        pass
    def get_display_name(self):
        return self.name
class Pizza(MenuItem):
    def __init__(self, name, base_price, size):
        super().__init__(name, base_price)
        self.size = size
    def calculate_price(self):
        if self.size == "large":
            return self.base_price * 1.30
        return self.base_price
class Drink(MenuItem):
    def __init__(self, name, base_price, is_ice):
        super().__init__(name, base_price)
        self.is_ice = is_ice
    def calculate_price(self):
        return self.base_price
    def get_display_name(self):
        if self.is_ice:
            return f"{self.name} со льдом"
        return self.name
class ComboSet(MenuItem):
    def __init__(self, name, items):
        super().__init__(name, 0)
        self.items = items
    def calculate_price(self):
        total = sum(item.calculate_price() for item in self.items)
        return total * 0.85