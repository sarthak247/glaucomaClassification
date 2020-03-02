import os

rename = 0

for image in os.listdir('.'):
    if '.py' in image:
        continue
    else:
        if '.png' in image:
            rename += 1
            print('Renaming: ',image)
            os.rename(image,'{}.png'.format(rename))
        elif '.jpg' in image:
            rename += 1
            print('Renaming: ',image)
            os.rename(image,'{}.jpg'.format(rename))