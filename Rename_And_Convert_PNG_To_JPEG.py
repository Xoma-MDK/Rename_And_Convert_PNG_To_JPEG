import os
from PIL import Image

path = 'C:/Users/molot/Desktop/Настя'

for dirName in os.listdir(path):
    i = 0
    for fileName in os.listdir(path + '/' + dirName):
        if i < 10:
            os.rename(path + '/' + dirName + '/'+fileName,
                      path + '/' + dirName + '/0' + str(i)+'.png')
        elif i >= 10:
            os.rename(path + '/' + dirName + '/'+fileName,
                      path + '/' + dirName + '/' + str(i)+'.png')
        i = i + 1
    os.mkdir(path + '/' + dirName + '/PNG')
    for fileName in os.listdir(path + '/' + dirName):
        if fileName != 'PNG':
            os.replace(path + '/' + dirName + '/' + fileName,
                       path + '/' + dirName + '/PNG/' + fileName)

for dirName in os.listdir(path):
    i = 0
    os.mkdir(path + '/' + dirName + '/JPEG')
    for fileName in os.listdir(path + '/' + dirName + '/PNG'):
        im = Image.open(path + '/' + dirName + '/PNG/' + fileName)
        im.convert('RGB').save(path + '/' + dirName +
                               '/JPEG/' + fileName[:-3] + '.jpeg', "JPEG")
