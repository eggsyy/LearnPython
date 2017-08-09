# coding=utf-8
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
s9 = 0
s10 = 0

# 执行操作
for i in range(10):
    url1 = "http://119.29.114.101:8004/game?acid=1121&ver=2.0.2"
    data1 = json.dumps(({"data": {"friendUid": "7-459347", "token": "c9ad09c93e38cafd6b23558b27b1ee97",
                                  "uid": "7-810089"}, "sign": "fc28b701ea62cbc0032eb8f8f58be6e7", "ts": 16}
                        ))
    r1 = requests.post(url1, data1)

    # 取返回值 addLevel和addValue
    b1 = (r1.json()["data"]["luaMatchvo"]["matchlog"]["atkScore"])
    b2 = (r1.json()["data"]["luaMatchvo"]["matchlog"]["defScore"])
    b3 = (r1.json()["data"]["luaMatchvo"]["matchlog"]["peraltyStatus"])

    # ATK胜
    if b1 > b2:
        s1 = s1 + 1

    else:
        pass

    # ATK非点球胜负
    if b3 == 0:
        if b1 > b2:
            s2 = s2 + 1
        else:
            pass
    else:
        pass

    # Def胜
    if b1 < b2:
        s3 = s3 + 1

    else:
        pass

    # Def非点球胜负
    if b3 == 0:
        if b1 < b2:
            s4 = s4 + 1
        else:
            pass
    else:
        pass

    # 比分差为1
    if b3 == 0:
        if abs(b1 - b2) == 1:
            s5 = s5 + 1
        else:
            pass
    else:
        pass

    # 比分差为2
    if b3 == 0:
        if abs(b1 - b2) == 2:
            s6 = s6 + 1
        else:
            pass
    else:
        pass

    # 比分差为3
    if b3 == 0:
        if abs(b1 - b2) == 3:
            s7 = s7 + 1
        else:
            pass
    else:
        pass

    # 比分差为4
    if b3 == 0:
        if abs(b1 - b2) == 4:
            s8 = s8 + 1
        else:
            pass
    else:
        pass

    # 比分差为5
    if b3 == 0:
        if abs(b1 - b2) == 5:
            s9 = s9 + 1
        else:
            pass
    else:
        pass

    # 比分差为6
    if b3 == 0:
        if abs(b1 - b2) == 6:
            s10 = s10 + 1
        else:
            pass
    else:
        pass

    # 打印返回json值
    print ('【', '比分：', b1, ":", b2, '】', '比分差：', b1 - b2, '点球：', b3,)
print ('主队非点球胜:', s2)
print ('客队非点球胜:', s4)
print ('主队点球胜:', s1 - s2)
print ('客队点球胜:', s3 - s4)
print ('比分相差一球:', s5)
print ('比分相差二球:', s6)
print ('比分相差三球:', s7)
print ('比分相差四球:', s8)
print ('比分相差五球:', s9)
print ('比分相差六球:', s10)
