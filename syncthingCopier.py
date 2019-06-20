import shutil, os
import send2trash

os.chdir('/home/chris/Sync')

try:

    shutil.copytree('WebDev', '/home/chris/SyncLaptop')
except:
    shutil.copytree('WebDev', '/home/chris/Sync')

#remember that shutil.move can overwrite whats in that the destinations directory
#also remember that when flushing this program out use the the send2trash module as it will send the previous version to the trash can

"""
try this out in your spare time

for foldername, subfolders, filenames in os.walk('/home/chris/PycharmProjects'):
    print('The current folder is ' + foldername)
    for subfolder in subfolders:
        print('SUBFOLDER OF ' + foldername + ": " + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + foldername + ': ' + filename)
    print('')

"""