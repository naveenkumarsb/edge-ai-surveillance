class RiskEngine:
    """
    Simple rule-based risk assessment engine.

    This is a prototype. The scoring model should be
    validated using appropriate test data before deployment.
    """

    def evaluate(self, event):
        score = 0

        if event["event_type"] == "ZONE_INTRUSION":
            score += 50

        if event.get("zone") == "Restricted Zone":
            score += 25

        if score >= 75:
            level = "HIGH"
        elif score >= 50:
            level = "MEDIUM"
        else:
            level = "LOW"

        return {
            **event,
            "risk_score": score,
            "risk_level": level,
        }