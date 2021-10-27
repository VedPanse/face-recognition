# API Key hidden

import requests

url = "https://microsoft-face1.p.rapidapi.com/detect"

querystring = {"returnFaceAttributes":"age","detectionModel":"detection_01","recognitionModel":"recognition_01","returnFaceId":"true"}

payload = "{\n    \"url\": \"https://upload.wikimedia.org/wikipedia/commons/6/6e/Shah_Rukh_Khan_graces_the_launch_of_the_new_Santro.jpg\"\n}"
headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "microsoft-face1.p.rapidapi.com",
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)
