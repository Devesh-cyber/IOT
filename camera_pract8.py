# Practical 8: Raspberry Pi with Pi Camera

# sudo apt install python3-picamera2

from picamera2 import Picamera2
from time import sleep

# Create camera object
camera = Picamera2()

# Configure camera
config = camera.create_preview_configuration(
    main={"size": (1024, 768)}
)
camera.configure(config)

# Start camera
camera.start()

# Wait for camera to initialize
sleep(5)

# Capture image
camera.capture_file("image1.jpg")

# Stop camera
camera.stop()