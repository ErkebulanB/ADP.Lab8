from abc import ABC, abstractmethod

class IPaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount): ...
    @abstractmethod
    def refund_payment(self, amount): ...

class InternalPaymentProcessor(IPaymentProcessor):
    def process_payment(self, amount):
        print(f"Ішкі жүйе: {amount} төлем өңделді")
    def refund_payment(self, amount):
        print(f"Ішкі жүйе: {amount} қайтарым өңделді")

class ExternalPaymentSystemA:
    def make_payment(self, amount):
        print(f"Сыртқы A: {amount} төлем жасалды")
    def make_refund(self, amount):
        print(f"Сыртқы A: {amount} қайтарым жасалды")

class ExternalPaymentSystemB:
    def send_payment(self, amount):
        print(f"Сыртқы B: {amount} төлем жіберілді")
    def process_refund(self, amount):
        print(f"Сыртқы B: {amount} қайтарым өңделді")

class PaymentAdapterA(IPaymentProcessor):
    def __init__(self, sys_a):
        self.sys_a = sys_a
    def process_payment(self, amount):
        self.sys_a.make_payment(amount)
    def refund_payment(self, amount):
        self.sys_a.make_refund(amount)

class PaymentAdapterB(IPaymentProcessor):
    def __init__(self, sys_b):
        self.sys_b = sys_b
    def process_payment(self, amount):
        self.sys_b.send_payment(amount)
    def refund_payment(self, amount):
        self.sys_b.process_refund(amount)

def choose_processor():
    print("Аймақты немесе валютаны таңдаңыз:")
    print("1) KZ / KZT")
    print("2) USA / USD")
    print("3) EU / EUR")
    x = input("Таңдау: ").strip()
    if x == "1":
        return InternalPaymentProcessor()
    elif x == "2":
        return PaymentAdapterA(ExternalPaymentSystemA())
    elif x == "3":
        return PaymentAdapterB(ExternalPaymentSystemB())
    else:
        print("Әдепкі: ішкі жүйе")
        return InternalPaymentProcessor()

def format_amount():
    s = input("Сома: ").strip()
    try:
        v = float(s)
        return v
    except:
        print("Дұрыс емес сома, әдепкі 0")
        return 0.0

def menu():
    processor = choose_processor()
    while True:
        print("\nМәзір:")
        print("1) Төлем жасау")
        print("2) Қайтарым жасау")
        print("3) Жүйені ауыстыру")
        print("0) Шығу")
        x = input("Таңдау: ").strip()
        if x == "1":
            amt = format_amount()
            processor.process_payment(amt)
        elif x == "2":
            amt = format_amount()
            processor.refund_payment(amt)
        elif x == "3":
            processor = choose_processor()
        elif x == "0":
            print("Бағдарлама аяқталды")
            break
        else:
            print("Дұрыс емес енгізу")

if __name__ == "__main__":
    menu()
