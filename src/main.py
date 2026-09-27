import cv2

from detection.detector import ObjectDetector


def main():
    detector = ObjectDetector()

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("ERROR: Could not open camera.")
        return

    print("Edge-AI surveillance started.")
    print("Press 'q' to exit.")

    while True:
        success, frame = camera.read()

        if not success:
            print("ERROR: Could not read camera frame.")
            break

        results = detector.detect(frame)

        annotated_frame = results[0].plot()

        cv2.imshow(
            "Edge-AI Surveillance",
            annotated_frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()