import os

import razorpay
from dotenv import load_dotenv

load_dotenv()


class RazorpayTestProvider:
    def __init__(self):
        key_id = os.getenv("RAZORPAY_KEY_ID")
        key_secret = os.getenv("RAZORPAY_KEY_SECRET")

        if not key_id or not key_secret:
            raise ValueError(
                "Razorpay credentials are missing from environment variables."
            )

        self.client = razorpay.Client(
            auth=(key_id, key_secret)
        )