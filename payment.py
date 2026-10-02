from abc import ABC, abstractmethod
import random
import string


class Payment(ABC):
    def __init__(self, rental):
        self.rental = rental
        self.amount = rental.calculate_total()

        if self.amount < 0:
            raise ValueError("Payment amount cannot be negative.")

    @abstractmethod
    def process_payment(self):
        pass


class MpesaPayment(Payment):
    def __init__(self, rental, phone_number):
        super().__init__(rental)
        self.phone_number = phone_number

    def process_payment(self):
        transaction_code = (
            ''.join(
                random.choices(
                    string.ascii_uppercase + string.digits,
                    k=10
                )
            )
        )

        print("\nProcessing M-Pesa payment...")
        print(f"Phone Number: {self.phone_number}")
        print(f"Transaction: {transaction_code}")
        print(f"Payment of KSh {self.amount:,.2f} successful.")

        return True


class CardPayment(Payment):
    def __init__(self, rental, last_four_digits):
        super().__init__(rental)
        self.last_four_digits = str(last_four_digits)

    def process_payment(self):
        print("\nProcessing card payment...")
        print(
            f"Card ending {self.last_four_digits} "
            f"charged KSh {self.amount:,.2f}"
        )

        print("Card payment successful.")

        return True


class CashPayment(Payment):
    def __init__(self, rental, cash_received):
        super().__init__(rental)

        if cash_received < 0:
            raise ValueError(
                "Cash received cannot be negative."
            )

        self.cash_received = cash_received

    def process_payment(self):

        print("\nProcessing cash payment...")

        if self.cash_received < self.amount:

            print(
                f"Cash received: KSh "
                f"{self.cash_received:,.2f}"
            )

            print(
                f"Amount required: KSh "
                f"{self.amount:,.2f}"
            )

            print("Cash payment failed.")

            return False

        change = self.cash_received - self.amount

        print(
            f"Cash received: KSh "
            f"{self.cash_received:,.2f}"
        )

        print(
            f"Change due:    KSh "
            f"{change:,.2f}"
        )

        print(
            f"Cash payment of KSh "
            f"{self.amount:,.2f} recorded."
        )

        return True