class SecurityZone:
    """Defines a rectangular security zone."""

    def __init__(self, x1, y1, x2, y2, name="Restricted Zone"):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.name = name

    def contains(self, x, y):
        """Check whether a point is inside the zone."""
        return (
            self.x1 <= x <= self.x2
            and self.y1 <= y <= self.y2
        )

    def check_object(self, bbox):
        """Check whether the center of a bounding box is inside the zone."""
        x1, y1, x2, y2 = bbox

        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2

        return self.contains(center_x, center_y)