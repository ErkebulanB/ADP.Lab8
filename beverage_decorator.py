from abc import ABC, abstractmethod

class IBeverage(ABC):
    @abstractmethod
    def get_cost(self): ...
    @abstractmethod
    def get_description(self): ...

class Coffee(IBeverage):
    def get_cost(self):
        return 50.0
    def get_description(self):
        return "Кофе"

class BeverageDecorator(IBeverage):
    def __init__(self, beverage):
        self.beverage = beverage
    def get_cost(self):
        return self.beverage.get_cost()
    def get_description(self):
        return self.beverage.get_description()

class MilkDecorator(BeverageDecorator):
    def get_cost(self):
        return super().get_cost() + 10.0
    def get_description(self):
        return super().get_description() + ", Сүт"

class SugarDecorator(BeverageDecorator):
    def get_cost(self):
        return super().get_cost() + 5.0
    def get_description(self):
        return super().get_description() + ", Қант"

class ChocolateDecorator(BeverageDecorator):
    def get_cost(self):
        return super().get_cost() + 15.0
    def get_description(self):
        return super().get_description() + ", Шоколад"

class VanillaDecorator(BeverageDecorator):
    def get_cost(self):
        return super().get_cost() + 12.0
    def get_description(self):
        return super().get_description() + ", Ваниль"

class CinnamonDecorator(BeverageDecorator):
    def get_cost(self):
        return super().get_cost() + 7.0
    def get_description(self):
        return super().get_description() + ", Даршын"

def format_cost(x):
    if float(x).is_integer():
        return f"{int(x)} ₸"
    return f"{x:.2f} ₸"

def menu():
    beverage = Coffee()
    while True:
        print("\nНегізгі сусын:", beverage.get_description(), "-", format_cost(beverage.get_cost()))
        print("Қоспа таңдаңыз:")
        print("1) Сүт (+10)")
        print("2) Қант (+5)")
        print("3) Шоколад (+15)")
        print("4) Ваниль (+12)")
        print("5) Даршын (+7)")
        print("6) Дайын")
        x = input("Таңдау: ").strip()
        if x == "1":
            beverage = MilkDecorator(beverage)
        elif x == "2":
            beverage = SugarDecorator(beverage)
        elif x == "3":
            beverage = ChocolateDecorator(beverage)
        elif x == "4":
            beverage = VanillaDecorator(beverage)
        elif x == "5":
            beverage = CinnamonDecorator(beverage)
        elif x == "6":
            print("\nСипаттама:", beverage.get_description())
            print("Жалпы баға:", format_cost(beverage.get_cost()))
            break
        else:
            print("Дұрыс емес енгізу")

if __name__ == "__main__":
    menu()
