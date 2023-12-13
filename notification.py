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



import requests
import json

ACCESS_TOKEN = 'o.K8sYAATHDyYjX7eURSn0g6z5wSnbnkXD'
resp = requests.post('https://api.pushbullet.com/v2/upload-request', data=json.dumps({'file_name': 'image.jpg'}), headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 'Content-Type': 'application/json'})
if resp.status_code != 200:
    raise Exception('failed to request upload')
r = resp.json()
resp = requests.post(r['upload_url'], data=r['data'], files={'file': open('image.jpg', 'rb')})
if resp.status_code != 204:
    raise Exception('failed to upload file')
print r['file_name'], r['file_type'], r['file_url']



# It's actually a 3 step process. You send a file upload request to pushbullet, they respond with an amazon URL, you send the file to amazon, and then send a pushbullet notification to a device.