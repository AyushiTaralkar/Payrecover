from dataclasses import dataclass

from app.payments.razorpay import RazorpayTestProvider


@dataclass
class PaymentResult:
    success: bool
    payment_id: str
    message: str


class PaymentService:
    def __init__(self):
        self.provider = RazorpayTestProvider()

    def retry_payment(
        self,
        payment_id: str,
        amount: int,
        idempotency_key: str,
    ) -> PaymentResult:

        result = self.provider.retry_payment(
            payment_id=payment_id,
            amount=amount,
            idempotency_key=idempotency_key,
        )

        return result