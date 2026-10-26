class Order:
    STATUSES = ["Создан", "Готовится", "Доставляется", "Завершен"]
    def __init__(self):
        self.__items = []
        self.__status = self.STATUSES[0]
    @property
    def status(self):
        return self.__status
    def add_item(self, item):
        if self.__status != self.STATUSES[0]:
            raise ValueError(
                f"Нельзя добавить '{item.get_display_name()}': заказ уже в статусе '{self.__status}'"
            )
        self.__items.append(item)
    def next_step(self):
        index = self.STATUSES.index(self.__status)
        if index < len(self.STATUSES) - 1:
            self.__status = self.STATUSES[index + 1]
        else:
            raise ValueError("Заказ уже завершён")
    def get_total_cost(self):
        return sum(item.calculate_price() for item in self.__items)
    def pay(self, payment_method):
        return payment_method.collect_payment(self.get_total_cost())