# Import Libraries
from PIL import Image
import os

target = '.png' # Target Format

scr_dir = os.getcwd() # Current Working Directory
dir_contents = os.listdir('data') # Contents of current working directory

# Maintain Log
f = open('convert_log.txt','w')

# Segregate out the data directories
dataDirectories = [] 
for directory in dir_contents:
    for srcData in os.listdir(src_dir + '/data/' + directory):
        dataDirectories.append(src_dir + '/data/' + directory + '/' + srcData)

# Convert from .jpg to .png
for directory in dataDirectories:
    os.chdir(directory)
    for image in listdir('.'):
        if '.jpg' in image:
            filename, extension = os.path.splitext(image)
            try:
                if extension not in ['.py', target]:
                    im = Image.open(filename + extension)
                    im.save(filename + target)
                    f.write('Converted: ' + filename + extension + '\n')
            except OSError:
                f.write('Cannot Convert ' + image + '\n')
    f.write('\n') # New Line designating a change in directory

# Close file pointer
f.close()
