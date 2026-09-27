from ultralytics import YOLO


class ObjectDetector:
    """YOLO-based object detector."""

    def __init__(self, model_path="yolo11n.pt", confidence=0.5):
        self.model = YOLO(model_path)
        self.confidence = confidence

    def detect(self, frame):
        """Run object detection on a single frame."""
        results = self.model.predict(
            source=frame,
            conf=self.confidence,
            verbose=False
        )

        return results


if __name__ == "__main__":
    detector = ObjectDetector()
    print("Object detector initialized successfully.")