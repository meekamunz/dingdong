#!/usr/bin/env python3
from notification import request_image_upload_url, send_doorbell_image_notification
from camera import take_picture
from functions import time_now
from rf_trigger import doorbell_trigger
import sys, logging

# Logging Configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('doorbell.log'),
        logging.StreamHandler()
        ]
    )    

# TO-DO:
# get arguments from command line
# Get RF notification
# Sort out file locations (web-server)
# File cleanup

# Temp Testing Data
# access_token = 'o.K8sYAATHDyYjX7eURSn0g6z5wSnbnkXD'
# channel_tag = 'hawthorne-doorbell'

# Arguments
# Arguments
def check_args():
    num_args = len(sys.argv)
    if num_args > 3:
        # Access Token from command line
        access_token = sys.argv[1]
        logging.debug(f'Access Token: {access_token}')

        # Channel Tag from command line
        channel_tag = sys.argv[2]
        logging.debug(f'Channel Tag: {channel_tag}')
        
        # RF signal ID
        rf_signal_id = sys.argv[3]
        logging.debug(f'RF Signal ID: {rf_signal_id}')
        
        # return access_token, channel_tag
        return access_token, channel_tag
    else:
        logging.warning(f'Not enough arguments. Usage: {sys.argv[0]} <access token> <channel tag>')
        logging.info('Exiting the application.')
        sys.exit(1)


def main():
    access_token, channel_tag, rf_signal_id = check_args()
    if doorbell_trigger(rf_signal_id) == False:
        doorbell_image = take_picture(time_now())
        image_url_link = request_image_upload_url(access_token, doorbell_image)
        send_doorbell_image_notification(access_token, channel_tag, image_url_link)

if __name__ == '__main__':
    logging.info('Starting the application')
    main()