class EventDetector:
    """Detects security events while preventing repeated alerts."""

    def __init__(self, restricted_classes=None):
        self.restricted_classes = restricted_classes or [0]
        self.active_intrusions = set()

    def check_zone_intrusion(self, tracked_objects, zone):
        events = set()
        current_intrusions = set()

        for obj in tracked_objects:
            class_id = obj["class_id"]
            object_id = obj["id"]
            bbox = obj["bbox"]

            if class_id not in self.restricted_classes:
                continue

            if object_id is None:
                continue

            inside_zone = zone.check_object(bbox)

            if inside_zone:
                current_intrusions.add(object_id)

                # Generate an event only when the object
                # enters the zone for the first time.
                if object_id not in self.active_intrusions:
                    events.add(
                        (
                            "ZONE_INTRUSION",
                            object_id,
                            class_id,
                            zone.name,
                        )
                    )

        # Update active objects.
        self.active_intrusions = current_intrusions

        return [
            {
                "event_type": event_type,
                "object_id": object_id,
                "class_id": class_id,
                "zone": zone_name,
            }
            for event_type, object_id, class_id, zone_name in events
        ]