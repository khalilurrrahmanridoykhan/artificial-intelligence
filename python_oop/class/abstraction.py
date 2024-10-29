from abc import abstractmethod, ABC

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Credit card payment of ${amount}"

class MobileWalletPaymentProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Mobile wallet payment of ${amount}"


payment1 = CreditCardPaymentProcessor()
print(payment1.process_payment(100))

payment2 = MobileWalletPaymentProcessor()
print(payment2.process_payment(200))