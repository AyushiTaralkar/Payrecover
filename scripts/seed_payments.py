from app.database.db import SessionLocal
from app.database.models import Payment


PAYMENTS = [
    {
        "payment_id": "P001",
        "customer_id": "C001",
        "amount": 1499,
        "currency": "INR",
        "status": "failed",
        "failure_reason": "insufficient_funds",
    },
    {
        "payment_id": "P002",
        "customer_id": "C002",
        "amount": 799,
        "currency": "INR",
        "status": "failed",
        "failure_reason": "bank_timeout",
    },
    {
        "payment_id": "P003",
        "customer_id": "C003",
        "amount": 2499,
        "currency": "INR",
        "status": "failed",
        "failure_reason": "mandate_inactive",
    },
    {
        "payment_id": "P004",
        "customer_id": "C004",
        "amount": 999,
        "currency": "INR",
        "status": "failed",
        "failure_reason": "insufficient_funds",
    },
    {
        "payment_id": "P005",
        "customer_id": "C005",
        "amount": 1299,
        "currency": "INR",
        "status": "failed",
        "failure_reason": "bank_timeout",
    },
    {
        "payment_id": "P006",
        "customer_id": "C006",
        "amount": 599,
        "currency": "INR",
        "status": "failed",
        "failure_reason": "mandate_inactive",
    },
    {
        "payment_id": "P007",
        "customer_id": "C007",
        "amount": 1899,
        "currency": "INR",
        "status": "failed",
        "failure_reason": "insufficient_funds",
    },
    {
        "payment_id": "P008",
        "customer_id": "C008",
        "amount": 2999,
        "currency": "INR",
        "status": "failed",
        "failure_reason": "bank_timeout",
    },
    {
        "payment_id": "P009",
        "customer_id": "C009",
        "amount": 699,
        "currency": "INR",
        "status": "failed",
        "failure_reason": "insufficient_funds",
    },
    {
        "payment_id": "P010",
        "customer_id": "C010",
        "amount": 1599,
        "currency": "INR",
        "status": "failed",
        "failure_reason": "mandate_inactive",
    },
]


def seed_payments():
    db = SessionLocal()

    try:
        for payment_data in PAYMENTS:
            existing_payment = (
                db.query(Payment)
                .filter(
                    Payment.payment_id == payment_data["payment_id"]
                )
                .first()
            )

            if existing_payment:
                print(
                    f"Skipping {payment_data['payment_id']} "
                    "(already exists)"
                )
                continue

            payment = Payment(**payment_data)
            db.add(payment)

        db.commit()

        print(f"Seeded {len(PAYMENTS)} payments successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_payments()