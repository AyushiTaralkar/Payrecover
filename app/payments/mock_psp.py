class MockPaymentProvider:

    def retry_payment(self, payment_id: str, amount: int):
        return {
            "success": True,
            "payment_id": payment_id,
            "message": f"Payment of ₹{amount} successfully retried."
        }