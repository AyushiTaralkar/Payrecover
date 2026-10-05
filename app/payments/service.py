from dataclasses import dataclass


@dataclass
class PaymentResult:
    success: bool
    payment_id: str
    message: str


class PaymentService:
    def __init__(self):
        pass

    def retry_payment(
        self,
        payment_id: str,
        amount: int,
        idempotency_key: str,
    ) -> PaymentResult:
        raise NotImplementedError