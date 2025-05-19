import anki_vector
from anki_vector.util import degrees
from ultralytics import YOLO
import cv2
import numpy as np
import keyboard
import time

def main():
    # Load YOLOv8 model
    model = YOLO("best.pt")  # Update path as needed

    # Connect to Vector
    with anki_vector.Robot("VECTOR_SERIAL_#") as robot:
        robot.behavior.set_head_angle(degrees(7.0))
        robot.behavior.set_lift_height(0.0)
        robot.camera.init_camera_feed()
        print("Camera feed initialized.")
        print("Starting real-time detection. Press 'q' to quit.")

        last_frame_time = time.time()
        motion_speed = 100

        while True:
            # Movement - check keys
            left_wheel = 0
            right_wheel = 0

            if keyboard.is_pressed("up"):
                left_wheel = right_wheel = motion_speed
            elif keyboard.is_pressed("down"):
                left_wheel = right_wheel = -motion_speed
            elif keyboard.is_pressed("left"):
                left_wheel = -50
                right_wheel = 50
            elif keyboard.is_pressed("right"):
                left_wheel = 50
                right_wheel = -50

            robot.motors.set_wheel_motors(left_wheel, right_wheel)

            # Limit FPS to ~5-10 fps to reduce CPU load
            current_time = time.time()
            if current_time - last_frame_time >= 0.1:  # ~10 FPS
                last_frame_time = current_time

                camera_image = robot.camera.latest_image
                if camera_image is not None:
                    pil_image = camera_image.raw_image
                    frame = np.array(pil_image)
                    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

                    # Run YOLO inference
                    results = model(frame, conf=0.5)
                    annotated = results[0].plot()

                    # Show prediction
                    cv2.imshow("Vector YOLOv8", annotated)

            # Check for exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        robot.motors.set_wheel_motors(0, 0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
