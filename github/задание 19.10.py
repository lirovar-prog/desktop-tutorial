class animal:
    def __init__(self, name, age, weight, diet,habitat):
        self.name=name
        self.age=age
        self.weight=weight
        self.diet=diet
        self.habitat=habitat
    def make_sound(self):
        return f'{self.name} издает характерные звуки.'
    def eat(self):
        return f'{self.name} сейчас ест. Его рацион — {self.diet}.'
class rebtile(animal):
    def __init__(self, name, age, weight, diet,habitat,type_scale,type_underwater):
        super().__init__(name, age, weight, diet,habitat)
        self.type_scale=type_scale
        self.type_underwater=type_underwater
    def scale_type(self):
        return f'{self.name}-его тип кожи это{self.type_scale}'
    def underwater_type(self):
        return f'{self.name}он проводит больше времени на{self.type_underwater}'
class Amphibian(animal):
    def __init__(self, name, age, weight, diet,habitat,breathes,big):
        super().__init__(name, age, weight, diet, habitat)
        self.breathes=breathes
        self.big=big
    def scale_type(self):
        return f'{self.name} его тип дыхание {self.breathes}'
    def underwater_type(self):
        return f'{self.name} он размером {self.big}'
turtle=rebtile(
    name='Черепаха', 
    age='85', 
    weight='0.5', 
    diet='травоядный', 
    habitat='океан', 
    type_scale='панцирь', 
    type_underwater='28'
)
toad=Amphibian(
    name='Жаба', 
    age='1', 
    weight='0.2', 
    diet='насекомые', 
    habitat='пруд', 
    breathes='гладкая и влажная', 
    big='маленький'
)
print(turtle.eat())
print(toad.make_sound())
print(turtle.scale_type())
print(toad.underwater_type())
# и так далеее




# class ZooShow:
#     def __init__(self):
#         self.croc = Reptile("Крокодил Гена", 12, 250, "хищник", "реки тропиков", "панцирная", 35)
#         self.chameleon = Reptile("Хамелеон Леон", 2, 0.4, "насекомоядный", "деревья", "зернистая", 28)
#         self.toad = Amphibian("Жаба Клава", 3, 0.6, "насекомоядная", "болота", "бугристая влажная", "взрослая особь")
#         self.salamander = Amphibian("Тритон Гоша", 1, 0.1, "мелкие беспозвоночные", "чистые пруды", "гладкая слизистая", "взрослая особь")
#     def run(self):
#         print("--- ДОБРО ПОЖАЛОВАТЬ В НАШ СУПЕР ЗОО-ПАРК! ---")
#         print("\nКакое шоу вы хотите посетить?")
#         print("1. Шоу Пресмыкающихся ")
#         print("2. Шоу Земноводных ")
#         choice = input("Введите номер варианта (1 или 2): ").strip()
#         if choice == "1":
#             show_type = "Пресмыкающиеся"
#             print(f"\n[ПРОГРАММА ШОУ '{show_type.upper()}']:")
#             print(f"- {self.croc.bask_in_sun()} А затем покажет смертельный трюк в воде!")
#             print(f"- {self.chameleon.shed_skin()} прямо во время маскировки на фоне декораций!")
#         elif choice == "2":
#             show_type = "Земноводные"
#             print(f"\n[ПРОГРАММА ШОУ '{show_type.upper()}']:")
#             print(f"- {self.toad.jump()} через огненный обруч на рекордную высоту!")
#             print(f"- {self.salamander.skin_breathe()} в прозрачном аквариуме под неоновыми лучами!")
#         else:
#             print("Неверный выбор. Перезапустите программу.")
#             return
#         print("\n--- Выбор билетов и цен ---")
#         print("Доступные категории мест:")
#         print("1. VIP-зона (Мягкие диваны у самой сцены, напиток в подарок) — 1500 рублей")
#         print("2. Обычные места (Комфортные кресла в амфитеатре) — 600 рублей")
#         ticket_choice = input("Выберите категорию (1 или 2): ").strip()
#         if ticket_choice == "1":
#             seat_type = "VIP-зона"
#             price = 1500
#         elif ticket_choice == "2":
#             seat_type = "Обычное место"
#             price = 600
#         else:
#             print("Неверный выбор категории.")
#             return
#         print("\n==============================================")
#         print("БИЛЕТ УСПЕШНО ОФОРМЛЕН!")
#         print(f"Категория: {seat_type} | Стоимость: {price} руб.")
#         if show_type == "Пресмыкающиеся":
#             print(f'\n"ШОУ ПРЕСМЫКАЮЩИХСЯ" {self.croc.name} и {self.chameleon.name} будут делать сальто в воду и синхронно менять цвет!')
#         else:
#             print(f'\n"ШОУ ЗЕМНОВОДНЫХ" {self.toad.name} и {self.salamander.name} будут играть на барабанах под водой и прыгать через препятствия!')
#         print("==============================================")
# if __name__ == "__main__":
#     show = ZooShow()
#     show.run()