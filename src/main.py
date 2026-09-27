import cv2

from detection.detector import ObjectDetector
from tracking.tracker import ObjectTracker
from risk_prediction.zone import SecurityZone
from events import EventDetector
from event_logger import EventLogger
from risk_prediction.risk_engine import RiskEngine


def main():
    # Initialize AI and security modules
    detector = ObjectDetector()
    tracker = ObjectTracker()

    # Define a restricted security zone
    zone = SecurityZone(
        x1=200,
        y1=100,
        x2=600,
        y2=450,
        name="Restricted Zone",
    )

    # Person class = 0 in the standard COCO dataset
    event_detector = EventDetector(
        restricted_classes=[0]
    )

    event_logger = EventLogger()
    risk_engine = RiskEngine()

    # Open laptop camera
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("ERROR: Could not open camera.")
        return

    print("====================================")
    print(" Intelligent Edge-AI Surveillance")
    print("====================================")
    print("Camera started.")
    print("Press 'q' to exit.")

    while True:

        # Read camera frame
        success, frame = camera.read()

        if not success:
            print("ERROR: Could not read camera frame.")
            break

        # Run object tracking
        results = detector.track(frame)

        # Extract tracked objects
        tracked_objects = tracker.process(results)

        # Check for security events
        events = event_detector.check_zone_intrusion(
            tracked_objects,
            zone
        )

        # Process detected events
        for event in events:

            # Calculate risk
            risk_event = risk_engine.evaluate(event)

            # Save event
            event_logger.log(risk_event)

            # Display event in terminal
           print("\n========== SECURITY EVENT ==========")
print(f"Event      : {risk_event['event_type']}")
print(f"Object ID  : {risk_event['object_id']}")
print(f"Zone       : {risk_event['zone']}")
print(f"Confidence : {risk_event['confidence']:.2f}")
print(f"Risk Score : {risk_event['risk_score']}")
print(f"Risk Level : {risk_event['risk_level']}")
print(
    "Reasons    : "
    + ", ".join(risk_event["risk_reasons"])
)
print("====================================\n")
            )

        # Draw detection results
        annotated_frame = results[0].plot()

        # Draw restricted zone
        cv2.rectangle(
            annotated_frame,
            (zone.x1, zone.y1),
            (zone.x2, zone.y2),
            (0, 0, 255),
            2,
        )

        # Label the zone
        cv2.putText(
            annotated_frame,
            zone.name,
            (zone.x1, zone.y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2,
        )

        # Show surveillance window
        cv2.imshow(
            "Intelligent Edge-AI Surveillance",
            annotated_frame
        )

        # Press q to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release resources
    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()