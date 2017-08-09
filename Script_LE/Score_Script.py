# coding=utf-8
import json

import requests

s1 = 0
s2 = 0
s3 = 0
s4 = 0
a = []
f = int(raw_input('请输入循环次数:'))
for i in range(f):
    url1 = "http://119.29.114.101:8004/game?acid=1121&ver=2.0.2"
    data1 = json.dumps(({"data": {"friendUid": "7-810089", "token": "a3a9cd6840ce2d110bacaf4a8b5d76da",
                                  "uid": "7-810749"}, "sign": "1906d9e93ba3731d8e6bcdf01f902380", "ts": 1754}))
    r1 = requests.post(url1, data1)

    atkScore = (r1.json()["data"]["luaMatchvo"]["matchlog"]["atkScore"])
    defScore = (r1.json()["data"]["luaMatchvo"]["matchlog"]["defScore"])
    atkShootPlayer = (r1.json()["data"]["luaMatchvo"]["atkShootPlayer"])
    defShootPlayer = (r1.json()["data"]["luaMatchvo"]["defShootPlayer"])
    penaltyStatus = (r1.json()["data"]["luaMatchvo"]["matchlog"]["peraltyStatus"])
    penaltyScore = (r1.json()["data"]["luaMatchvo"]["matchlog"]["peraltyScore"])
    Abs_score = abs(atkScore - defScore)

    # 打印比分
    print i + 1, '【', '比分：', atkScore, ":", defScore, '】', '比分差：', Abs_score, \
        '点球: ', penaltyStatus

    # 判断是否点球
    if penaltyStatus == 1:
        if atkScore > defScore:
            s3 = s3 + 1
        else:
            s4 = s4 + 1
        if penaltyScore == 0:
            print '没人进球，点球大战 '
            print ''
        else:
            print '进攻方进球球员分别是：',
            for x in atkShootPlayer:
                print x['name'],
            print ''
            print '防守方进球球员分别是：',
            for y in defShootPlayer:
                print y['name'],
            print ''
            print ''

    # 判断主场进球是否为0
    elif atkScore == 0:
        s2 = s2 + 1
        print '进攻方没有进球'
        print '防守方进球球员分别是：',
        for y in defShootPlayer:
            print y['name'],
        print ''
        print ''
        a.append(Abs_score)

    # 判断客场进球是否为0
    elif defScore == 0:
        s1 = s1 + 1
        print '防守方没有进球'
        print '进攻方进球球员分别是：',
        for x in atkShootPlayer:
            print x['name'],
        print ''
        print ''
        a.append(Abs_score)
    else:
        if atkScore > defScore:
            s1 = s1 + 1
        else:
            s2 = s2 + 1
        print '进攻方进球球员分别是：',
        for x in atkShootPlayer:
            print x['name'],
        print ''
        print '防守方进球球员分别是：',
        for y in defShootPlayer:
            print y['name'],
        print ''
        print ''
        a.append(Abs_score)

print '主队非点球胜: %d次' % s1
print '客队非点球胜: %d次' % s2
print '主队点球胜: %d次' % s3
print '客队点球胜: %d次' % s4
print '点球大战: %d次' % (s3 + s4)
for i in set(a):
    b = a.count(i)
    print '比分相差%d球:' % i, '%d 次' % b
