# encoding:utf-8
import requests
import json

s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0
s7 = 0
s8 = 0

# 执行操作
for i in range(10):
    url1 = "http://119.29.114.101:8004/game?acid=1078&ver=2.0.2"
    data1 = json.dumps({"data": {"id": "1", "token": "b0a95c5521e06cf7d632c77586582a7c", "uid": "7-810749"},
                        "sign": "71b2ddc8374fe274cd30d8236889ba5f", "ts": 65})
    r1 = requests.post(url1, data1)

    # 取返回值
    b1 = (r1.json()["data"]["propList"][0]["id"])
    b2 = (r1.json()["data"]["propList"][0]["id"])
    b3 = (r1.json()["data"]["propList"][0]["id"])
    b4 = (r1.json()["data"]["propList"][0]["id"])
    b5 = (r1.json()["data"]["propList"][0]["id"])
    b6 = (r1.json()["data"]["propList"][0]["id"])
    b7 = (r1.json()["data"]["propList"][0]["id"])
    b8 = (r1.json()["data"]["propList"][0]["id"])
    # 道具ID
    if b1 == 701:
        s1 = s1 + 1

    else:
        pass

    if b2 == 717:
        s2 = s2 + 1

    else:
        pass

    if b3 == 734:
        s3 = s3 + 1

    else:
        pass

    if b4 == 706:
        s4 = s4 + 1

    else:
        pass

    if b5 == 742:
        s5 = s5 + 1

    else:
        pass

    if b6 == 747:
        s6 = s6 + 1

    else:
        pass
    if b7 == 714:
        s7 = s7 + 1

    else:
        pass

    if b8 == 709:
        s8 = s8 + 1

    else:
        pass

    print (b1)
# 打印返回json值
print ('抽到升星宝石', s1, '次')
print ('抽到净化宝石', s2, '次')
print ('抽到巨星之证', s3, '次')
print ('抽到特训卡', s4, '次')
print ('抽到葡萄糖', s5, '次')
print ('抽到默契之证', s6, '次')
print ('抽到钻石', s7, '次')
print ('抽到体力', s8, '次')
