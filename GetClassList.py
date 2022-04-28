import json
import requests

crawlURL = 'https://knuin.knu.ac.kr/public/web/stddm/lsspr/syllabus/lectPlnInqr/selectItttnCdListLectPlnInqr'

getUnivListPayload = {
  "search": {
    "gubun": "02",
    "code": "02",
    "name": "´ëÇÐ",
    "estblYear": "2022",
    "estblSmstrSctcd": "CMBS001400001",
    "isApi": "Y",
    "rowStatus": "U"
  }
}

requestHeader = {'Content-Type': 'application/json'}
def GetUnivList():
    request = json.dumps(getUnivListPayload)
    response = requests.post(url, request, headers=requestHeader)
    if response.status_code>=400:
        print('failed to get file')
        return
    print(response)
    with open('./UnivList.json', 'w') as savefile:
        json.dump(response.json(), savefile, indent=4)