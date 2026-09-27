class ObjectTracker:
    """Processes tracking results and extracts tracked objects."""

    def process(self, results):
        tracked_objects = []

        if not results:
            return tracked_objects

        result = results[0]

        if result.boxes is None:
            return tracked_objects

        boxes = result.boxes

        for i in range(len(boxes)):
            box = boxes[i]

            object_id = None

            if boxes.id is not None:
                object_id = int(boxes.id[i].item())

            class_id = int(box.cls[i].item())
            confidence = float(box.conf[i].item())

            coordinates = box.xyxy[i].tolist()

            tracked_objects.append(
                {
                    "id": object_id,
                    "class_id": class_id,
                    "confidence": confidence,
                    "bbox": coordinates,
                }
            )

        return tracked_objects