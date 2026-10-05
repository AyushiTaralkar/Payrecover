import json
from pathlib import Path

from app.database.db import SessionLocal
from app.database.models import Customer


DATA_FILE = Path("data/customers.json")


def seed_customers():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        customers = json.load(file)

    db = SessionLocal()

    try:
        for customer_data in customers:
            existing_customer = (
                db.query(Customer)
                .filter(
                    Customer.customer_id == customer_data["customer_id"]
                )
                .first()
            )

            if existing_customer:
                print(
                    f"Skipping {customer_data['customer_id']} "
                    "(already exists)"
                )
                continue

            customer = Customer(**customer_data)

            db.add(customer)

        db.commit()

        print(f"Seeded {len(customers)} customers successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_customers()