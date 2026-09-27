class RiskEngine:
    """
    Rule-based risk assessment engine.

    This prototype converts contextual event features
    into a configurable risk score.
    """

    def __init__(
        self,
        intrusion_score=50,
        restricted_zone_score=25,
    ):
        self.intrusion_score = intrusion_score
        self.restricted_zone_score = restricted_zone_score

    def evaluate(self, event):
        score = 0
        reasons = []

        # 1. Zone intrusion
        if event.get("event_type") == "ZONE_INTRUSION":
            score += self.intrusion_score
            reasons.append("Restricted-zone intrusion")

        # 2. Restricted zone
        if event.get("zone") == "Restricted Zone":
            score += self.restricted_zone_score
            reasons.append("Restricted security zone")

        # 3. Detection confidence
        confidence = event.get("confidence", 0.0)

        if confidence >= 0.8:
            score += 10
            reasons.append("High detection confidence")

        # Limit score to 100
        score = min(score, 100)

        # Determine risk category
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
            "risk_reasons": reasons,
        }