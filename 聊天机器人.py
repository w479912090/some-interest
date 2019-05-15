from time import sleep
import requests

s = input('请主人输入话题:')
while True:
    resp = requests.post('http://www.tuling123.com/openapi/api', data={'key': 'a0e723afd35e499186d65e036485161e', 'info': s, })
    resp = resp.json()
    sleep(1)
    print('小鱼:', resp['text'])
    s = resp['text']
    resp = requests.get('http://api.qingyunke.com/api.php', {'key': 'free', 'appid': 0, 'msg': s})
    resp.encoding = 'utf-8'
    resp = resp.json()
    sleep(1)
    print('菲菲:', resp['content'])