import json
from pprint import pprint

import requests

def GetSchedule(filename, payload, header, url):
    request = json.dumps(payload)
    response = requests.post(url, request, headers=header)
    print(response)
    with open('./{0}.json'.format(filename), 'w') as savefile:
        json.dump(response.json(), savefile, indent=4)


def ReadSchedule(path):
    classes = []
    with open(path, 'r') as openfile:
        json_data = json.load(openfile)
        dic = {}
        for cls in json_data['data']:
            if cls['lssnsTimeInfo'] != None:
                t = (cls['lssnsTimeInfo']).split('<br/>')
                sche = []
                for i in t:
                    i0 = i.split(' ')
                    sche.append((i0[0], i0[1].split(',')))
                    dic['sche'] = sche
            else:
                dic['sche'] = None
            dic['name'] = cls['sbjetNm']
            dic['professor'] = cls['totalPrfssNm']
            classes.append(dic)
    for c in classes:
        print('[{0}]'.format(c['name']))
        if c['professor'] != '':
            print('교수 : {0}'.format(c['professor'].split('<br/>')))
        if c['sche'] != '':
            print('시간표 : {0}'.format(c['sche']), end='\n\n')


if __name__ == "__main__":
    requestStr = {
        "search": {
            "estblYear": "2022",
            "estblSmstrSctcd": "CMBS001400004",
            "sbjetCd": "",
            "sbjetNm": "",
            "crgePrfssNm": "",
            "sbjetRelmCd": "01",
            "sbjetSctcd": "",
            "estblDprtnCd": "",
            "rmtCrseYn": "",
            "rprsnLctreLnggeSctcd": "",
            "flplnCrseYn": "",
            "pstinNtnnvRmtCrseYn": "",
            "dgGbDstrcRmtCrseYn": "",
            "gubun": "01",
            "isApi": "Y",
            "bldngSn": "",
            "bldngCd": "",
            "bldngNm": "",
            "lssnsLcttmUntcd": "",
            "sbjetSctcd2": "",
            "contents": ""
        }
    }
    path = './교양.json'
    name = '계절'
    requestHeader = {'Content-Type': 'application/json',
                     'Accept': 'application/json, text/javascript, */*; q=0.01'}
    URL = 'https://knuin.knu.ac.kr/public/web/stddm/lsspr/syllabus/lectPlnInqr/selectListLectPlnInqr'
    # GetSchedule(name, requestStr, requestHeader, URL)
    ReadSchedule('./교양.json')

