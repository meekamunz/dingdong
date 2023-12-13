#curl --header 'Access-Token: <your_access_token_here>' \
#     https://api.pushbullet.com/v2/users/me
# Response
#{
#  "created": 1381092887.398433,
#  "email": "elon@teslamotors.com",
#  "email_normalized": "elon@teslamotors.com",
#  "iden": "ujpah72o0",
#  "image_url": "https://static.pushbullet.com/missing-image/55a7dc-45",
#  "max_upload_size": 26214400,
#  "modified": 1441054560.741007,
#  "name": "Elon Musk"
#}

# curl --header 'Access-Token: o.K8sYAATHDyYjX7eURSn0g6z5wSnbnkXD' https://api.pushbullet.com/v2/pushes -d type=note&title="dingdong-test"&channel_tag="hawthorne-doorbell"

#curl --header 'Access-Token: <your_access_token_here>' \
#     --header 'Content-Type: application/json' \
#     --data-binary '{"file_name":"cat.jpg","file_type":"image/jpeg"}' \
#     --request POST \
#
#     https://api.pushbullet.com/v2/upload-request



import requests, json

# Test Config
access_token = 'o.K8sYAATHDyYjX7eURSn0g6z5wSnbnkXD'
image = '2023-12-13_21-56-16.jpg'

# It's actually a 3 step process. You send a file upload request to pushbullet, they respond with an amazon URL, you send the file to amazon, and then send a pushbullet notification to a device.

POST https://api.pushbullet.com/v2/upload-request


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