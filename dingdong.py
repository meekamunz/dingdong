from notification import request_image_upload_url, send_doorbell_image_notification
from camera import take_picture
from functions import time_now
import sys

# TO-DO:
# get arguments from command line
# Get RF notification
# Sort out file locations (web-server)
# Logging

# Temp Testing Data
access_token = 'o.K8sYAATHDyYjX7eURSn0g6z5wSnbnkXD'
channel_tag = 'hawthorne-doorbell'

num_args = len(sys.argv)
if 1 > num_args > 3:
    # Access Token from command line
    access_token = sys.argv[1]
    
    # Channel Tag from command line
    channel_tag = sys.argv[2]
    
else: print(f'Not enough arguments. Usage: {sys.argv[0]} <access token> <channel tag>')     

def main():
    # Doorbell trigger here
    doorbell_image = take_picture(time_now())
    image_url_link = request_image_upload_url(access_token, doorbell_image)
    send_doorbell_image_notification(access_token, channel_tag, image_url_link)

if __name__ == '__main__':  
    main()