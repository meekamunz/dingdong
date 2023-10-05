from picamera2 import Picamera2
from libcamera import controls

def get_video(output_file, format, duration):
    #libcamera-vid -t duration -o output_file.format