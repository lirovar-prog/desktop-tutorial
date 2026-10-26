from abc import ABC, abstractmethod
from datetime import date
class PaymentStrategy(ABC):
    @abstractmethod
    def collect_payment(self, amount):
        pass
class CardPayment(PaymentStrategy):
    def __init__(self, card_number, expiry_date):
        self.card_number = card_number
        self.expiry_date = expiry_date  # формат "MM/YY"
    def collect_payment(self, amount):
        month_str, year_str = self.expiry_date.split("/")
        month = int(month_str)
        year = 2000 + int(year_str)
        today = date.today()
        if (year, month) < (today.year, today.month):
            print(f"Карта {self.card_number} просрочена. Оплата отклонена.")
            return False
        print(f"Списано {amount:.2f} с карты {self.card_number}.")
        return True
class CashPayment(PaymentStrategy):
    def collect_payment(self, amount):
        print(f"Оплата наличными: {amount:.2f}")
        return True