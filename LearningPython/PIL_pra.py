from PIL import Image
im = Image.open('1.png')
print im.format, im.size, im.mode
im.thumbnail((268, 494))
im.save('test.png')
