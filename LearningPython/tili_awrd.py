# -*- coding:utf-8 -*-
import requests
import json
import MySQLdb

a = []
# 数据库连接
conn = MySQLdb.connect(
    host='203.195.163.33',
    port=10010,
    user='gamer',
    passwd='pwq10Vmi',
    db='game1',
    charset='utf8',
)
cur = conn.cursor()

# 执行操作
f = int(raw_input('请输入循环次数:'))
for i in range(f):
    url1 = "http://119.29.114.101:8004/game?acid=1078&ver=2.0.2"
    data1 = json.dumps({"data": {"id": "1", "token": "d5ab451d15caa8f7945016d93a9f5996", "uid": "7-810749"}, "sign": "fd6398be0761668ec75ec3ca095ccb54", "ts": 108})
    r1 = requests.post(url1, data1)

    # 取返回值
    b1 = (r1.json()["data"]["propList"][0]["id"])
    a.append(b1)

# 依次打印获得的道具名称、获得次数和频率
for i in set(a):
    c = a.count(i)
    d = float(c) / float(f)
    e = d * 100
    cur.execute("select name from common_property where id = %s" % i)
    info = cur.fetchall()
    for g in info:
        g1 = g[0]
        print '获得', g1.encode("utf8"), c, '次,掉落频率为:''%.1f%%' % e
cur.close()
conn.commit()
conn.close()
