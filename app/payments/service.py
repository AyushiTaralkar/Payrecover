from app.payments.mock_psp import MockPaymentProvider


class PaymentService:

    def __init__(self):
        self.provider = MockPaymentProvider()

    def retry_payment(self, payment_id: str, amount: int):
        return self.provider.retry_payment(payment_id, amount)