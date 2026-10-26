from menu import Pizza, Drink, ComboSet
from pay import CardPayment, CashPayment
from order import Order
pizza = Pizza("Маргарита", 400, "large")
cola = Drink("Кола", 100, True)
combo = ComboSet("Комбо", [pizza, cola])
print(pizza.calculate_price())
print(cola.calculate_price())
print(cola.get_display_name())
print(combo.calculate_price())
order = Order()
order.add_item(pizza)
order.add_item(cola)
order.add_item(combo)
print("Итого:", order.get_total_cost())
order.pay(CardPayment("4444-5555-6666-7777", "12/29"))
order.pay(CashPayment())
order.next_step()
print("Статус:", order.status)
try:
    order.add_item(Drink("Кофе", 150, False))
except ValueError as e:
    print("Ошибка:", e)
try:
    order.status = "Завершен"
except AttributeError:
    print("Статус напрямую менять нельзя")