import requests
import base64
import cv2

url = 'http://10.59.10.113:32168/v1/image/cartoonise'

files = {'image': open('kosik.jpg', 'rb').read()}
data = {'model': ''}

try:
    response = requests.post(url, files=files, data=data)
    if response.ok:
        data = response.json()
        #print(data)
        if data["success"] == True :
            img=data["imageBase64"]
            fp=open("soubor.png",'wb')
            fp.write(base64.b64decode(img))
            fp.close()
except requests.exceptions.RequestException as e:
    print('Unable to complete API call: ' + str(e))