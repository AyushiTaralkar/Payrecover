from dataclasses import dataclass


@dataclass
class RecoveryDecision:
    action: str
    allowed: bool
    reason: str


class RecoveryEngine:

    def decide(self, failure_reason: str) -> RecoveryDecision:

        if failure_reason == "insufficient_funds":
            return RecoveryDecision(
                action="retry_payment",
                allowed=True,
                reason="Payment may be retried for insufficient funds.",
            )

        if failure_reason == "bank_timeout":
            return RecoveryDecision(
                action="payment_link",
                allowed=True,
                reason="Bank timeout should be handled through a payment link.",
            )

        if failure_reason == "mandate_inactive":
            return RecoveryDecision(
                action="human_escalation",
                allowed=True,
                reason="Inactive mandate requires human assistance.",
            )

        return RecoveryDecision(
            action="human_escalation",
            allowed=True,
            reason="Unknown payment failure reason.",
        )