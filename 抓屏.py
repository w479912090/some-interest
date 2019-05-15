from time import sleep
from PIL import ImageGrab

m = int(input('你想抓屏多少秒:'))
n = 1
while n < m:
    sleep(0.02)
    im = ImageGrab.grab()
    local = (r'%s.jpg' % (n))
    im.save(local, 'jpeg')
    n = n + 1
