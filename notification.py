import requests, json

# Test Config
access_token = 'o.K8sYAATHDyYjX7eURSn0g6z5wSnbnkXD'
image = '2023-12-13_21-56-16.jpg'
channel_tag = 'hawthorne-doorbell'

# Request file upload, returns a URL to upload the file to
def request_image_upload_url(access_token, image):    
    resp = requests.post('https://api.pushbullet.com/v2/upload-request', data=json.dumps({'file_name': image, 'file_type': 'image/jpeg'}), headers={'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('failed to request upload')
    r = resp.json()
    resp = requests.post(r['upload_url'], data=r['data'], files={'file': open(image, 'rb')})
    if resp.status_code != 204:
        raise Exception('failed to upload file')
    print(r['file_name'], r['file_type'], r['file_url'])
    return(r['file_url'])

# Send Pushbullet notification to hawthorne-doorbell channel_tag
def send_doorbell_image_notification(access_token, channel_tag, image_url):
    resp =requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps({'body': 'There\'s somebody at the door!', 'title': 'Ding-dong!', 'type': 'link', 'channel_tag': channel_tag, 'url': image_url}), headers={'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'})
    