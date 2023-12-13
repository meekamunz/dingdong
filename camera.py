from picamera2 import Picamera2
from picamera2.encoders import H264Encoder, Quality
from picamera2.outputs import FfmpegOutput
import time

# picam settings
picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)
encoder = H264Encoder(10000000)
output = FfmpegOutput("-f hls -hls_time 4 -hls_list_size 5 -hls_flags delete_segments -hls_allow_cache 0 stream.m3u8")
#output = FfmpegOutput("-f dash -window_size 5 -use_template 1 -use_timeline 1 stream.mpd")

# record video for x time
def rec_video(output_file, format, duration):
    picam2.start_recording(encoder, f'{output_file}.{format}')
    time.sleep(duration)
    picam2.stop_recording()


# start and stop video streaming
def video_stream(action):
    if action=='start': picam2.start_recording(encoder, output)
    elif action=="stop": picam2.stop_recording()
    else: print('ERROR: No command.')
    

# take a picture
def take_picture(file_name):
    picam2.start()
    time.sleep(2)
    picam2.capture_file(f'{file_name}.jpg')
    picam2.close()