import cv2

from detection.detector import ObjectDetector
from tracking.tracker import ObjectTracker


def main():
    detector = ObjectDetector()
    tracker = ObjectTracker()

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("ERROR: Could not open camera.")
        return

    print("Edge-AI surveillance with object tracking started.")
    print("Press 'q' to exit.")

    while True:
        success, frame = camera.read()

        if not success:
            print("ERROR: Could not read camera frame.")
            break

        results = detector.track(frame)

        objects = tracker.process(results)

        annotated_frame = results[0].plot()

        cv2.imshow(
            "Edge-AI Surveillance - Tracking",
            annotated_frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()