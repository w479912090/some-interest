from wxpy import *
import math
from PIL import Image
import os

def create_filepath():
    avatar_dir = os.getcwd() + '\\wechat\\'
    if not os.path.exists(avatar_dir):
        os.mkdir(avatar_dir)
    return avatar_dir

def save_avatar(avatar_dir):
    bot = Bot()
    friends = bot.friends(update=True)
    num=0
    for friend in friends:
        friend.get_avatar(avatar_dir + '\\' + str(num) + '.jpg')
        print('好友昵称：%s' % friend.nick_name)
        num = num + 1

def joint_avatar(path):
    length = len(os.listdir(path))
    image_size = 2560
    each_size = math.ceil(image_size/math.floor(math.sqrt(length)))
    x_lines = math.ceil(math.sqrt(length))
    y_lines = math.ceil(math.sqrt(length))
    image = Image.new('RGB', (each_size * x_lines, each_size * y_lines))
    x = 0
    y = 0
    for (root, dirs, files) in os.walk(path):
        for pic_name in files:
            try:
                with Image.open(path + pic_name) as img:
                    img = img.resize((each_size, each_size))
                    image.paste(img, (x * each_size, y * each_size))
                    x += 1
                    if x == x_lines:
                        x = 0
                        y += 1
            except IOError:
                print('头像读取失败')
    img = image.save(os.getcwd() + '/wechat.png')
    print('微信好友头像拼接完成')

if __name__ == '__main__':
    avatar_dir = create_filepath()
    save_avatar(avatar_dir)
    joint_avatar(avatar_dir)