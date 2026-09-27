from ultralytics import YOLO


class ObjectDetector:
    """YOLO-based object detection and tracking."""

    def __init__(self, model_path="yolo11n.pt", confidence=0.5):
        self.model = YOLO(model_path)
        self.confidence = confidence

    def detect(self, frame):
        """Run object detection on a frame."""
        return self.model.predict(
            source=frame,
            conf=self.confidence,
            verbose=False
        )

    def track(self, frame):
        """Run object tracking on a frame."""
        return self.model.track(
            source=frame,
            conf=self.confidence,
            persist=True,
            verbose=False
        )