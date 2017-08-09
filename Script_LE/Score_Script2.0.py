# coding=utf-8
import json
import requests

# 定义初始变量
s1 = 0
s2 = 0
s3 = 0
s4 = 0
a = []

# 获取JSON返回值
f = int(raw_input('请输入循环次数:'))
for i in range(f):
    url1 = "http://119.29.114.101:8004/game?acid=1121&ver=2.0.2"
    data1 = json.dumps(({"data": {"friendUid": "7-810089",
                                  "token": "a3a9cd6840ce2d110bacaf4a8b5d76da",
                                  "uid": "7-810749"}, "sign": "1906d9e93ba3731d8e6bcdf01f902380",
                         "ts": 1754}))
    r1 = requests.post(url1, data1)

    # 定义变量
    atkScore = (r1.json()["data"]["luaMatchvo"]["matchlog"]["atkScore"])
    defScore = (r1.json()["data"]["luaMatchvo"]["matchlog"]["defScore"])
    atkShootPlayer = (r1.json()["data"]["luaMatchvo"]["atkShootPlayer"])
    defShootPlayer = (r1.json()["data"]["luaMatchvo"]["defShootPlayer"])
    penaltyStatus = (r1.json()["data"]["luaMatchvo"]["matchlog"]["peraltyStatus"])
    penaltyScore = (r1.json()["data"]["luaMatchvo"]["matchlog"]["peraltyScore"])
    Abs_score = abs(atkScore - defScore)

    # 定义函数
    def no_goal():
        print '没人进球，点球大战 '
        print ''

    def atk_Score():
        print '进攻方进球球员分别是：',
        for x in atkShootPlayer:
            print x['name'],
        print ''

    def def_Score():
        print '防守方进球球员分别是：',
        for y in defShootPlayer:
            print y['name'],
        print ''
        print ''

    def atk_no_goal():
        print '进攻方没有进球'

    def def_no_goal():
        print '防守方没有进球'

    # 打印比分
    print i + 1, '【', '比分：', atkScore, ":", defScore, '】', '比分差：', Abs_score, \
        '点球: ', penaltyStatus

    # 判断是否点球
    if penaltyStatus == 1:
        if penaltyScore == 0:
            no_goal()
        else:
            atk_Score()
            def_Score()
        if atkScore > defScore:
            s3 = s3 + 1
        else:
            s4 = s4 + 1

    # 判断主场进球是否为0
    elif atkScore == 0:
        atk_no_goal()
        def_Score()
        s2 = s2 + 1
        a.append(Abs_score)

    # 判断客场进球是否为0
    elif defScore == 0:
        def_no_goal()
        atk_Score()
        s1 = s1 + 1
        a.append(Abs_score)
    else:
        atk_Score()
        def_Score()
        if atkScore > defScore:
            s1 = s1 + 1
        else:
            s2 = s2 + 1
        a.append(Abs_score)

for j in set(a):
    b = a.count(j)
print '主队非点球胜: %d次' % s1
print '客队非点球胜: %d次' % s2
print '主队点球胜: %d次' % s3
print '客队点球胜: %d次' % s4
print '点球大战: %d次' % (s3 + s4)
print '比分相差%d球:' % j, '%d 次' % b
