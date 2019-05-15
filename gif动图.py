from PIL import Image

im = Image.open('1.jpg')
Images = []
Images.append(Image.open('2.jpg'))
Images.append(Image.open('3.jpg'))
Images.append(Image.open('4.jpg'))
im.save('gif.gif', save_all = True, append_images = Images, loop = 1, duration = 1, comment = b'aaabb')