from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
#from libcamera import controls
from datetime import datetime
import time

picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)
encoder = H264Encoder(10000000)

def time_now():
    datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def get_video(output_file, format, duration):
    #libcamera-vid -t duration -o output_file.format
    #libcamera-vid -t 20000 -o  time_now().mp4
    picam2.start_recording(encoder, f'{output_file}.{format}')
    time.sleep(duration)
    picam2.stop_recording()