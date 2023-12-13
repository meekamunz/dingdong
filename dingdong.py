from notification import request_image_upload_url, send_doorbell_image_notification
from camera import take_picture
from functions import time_now

# TO-DO:
# Get RF notification
# Sort out file locations (web-server)
# Logging

# Temp Testing Data
access_token = 'o.K8sYAATHDyYjX7eURSn0g6z5wSnbnkXD'
channel_tag = 'hawthorne-doorbell'

if __name__ == '__main__':
    # Doorbell trigger here
    doorbell_image = take_picture(time_now())
    image_url_link = request_image_upload_url(access_token, doorbell_image)
    send_doorbell_image_notification(access_token, channel_tag, image_url_link)