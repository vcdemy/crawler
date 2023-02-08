from linenotify import Notify
import random
import os
import time

token = 'D4U0lsAuRsrpdDPrkqwSYkI2ZiXzzeSLKgz5XVBM5JW'
# message = '你好帥喔！'
messages = ['有沒有想我？', '我今天都在想你！','我真的覺得你好帥！']

path = os.path.dirname(__file__)

while True:
    Notify(token, random.choice(messages), img=path+"/"+str(random.randint(0,20))+".jpg")
    time.sleep(random.randint(3,10))
