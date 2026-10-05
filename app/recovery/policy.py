class RecoveryPolicy:

    MAX_RETRY_ATTEMPTS = 2

    def can_retry(
        self,
        failure_reason: str,
        retry_count: int,
        customer_confirmed: bool,
    ) -> tuple[bool, str]:

        if not customer_confirmed:
            return (
                False,
                "Customer confirmation is required before retrying.",
            )

        if retry_count >= self.MAX_RETRY_ATTEMPTS:
            return (
                False,
                "Maximum retry attempts reached.",
            )

        if failure_reason == "mandate_inactive":
            return (
                False,
                "Inactive mandate requires human assistance.",
            )

        if failure_reason == "bank_timeout":
            return (
                False,
                "Bank timeout should be handled through a payment link.",
            )

        if failure_reason != "insufficient_funds":
            return (
                False,
                "Payment failure reason is not eligible for retry.",
            )

        return (
            True,
            "Retry is allowed.",
        )