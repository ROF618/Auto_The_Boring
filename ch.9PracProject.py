"""
Practice Projects

For practice, write programs to do the following tasks.
Selective Copy

Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
Deleting Unneeded Files

It’s not uncommon for a few unneeded but humongous files or folders to take up the bulk of the space on your hard drive. If you’re trying to free up room on your computer, you’ll get the most bang for your buck by deleting the most massive of the unwanted files. But first you have to find them.

Write a program that walks through a folder tree and searches for exceptionally large files or folders—say, ones that have a file size of more than 100MB. (Remember, to get a file’s size, you can use os.path.getsize() from the os module.) Print these files with their absolute path to the screen.
Filling in the Gaps

Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt). Have the program rename all the later files to close this gap.

As an added challenge, write another program that can insert gaps into numbered files so that a new file can be added.

"""


import os, shutil
#find how to get the files extensions from the folder traversing loop
#extResults = []

for folderName, subfolders, filenames in os.walk('/home/chris/Pictures'):
    for file in filenames:
        if file.endswith(".jpg"):
            #the copy function works for the files in the directory but for the subdirectories more logic needs to introduced
            pathFile = os.path.join(folderName, file)
            #it still get caught up in the sub directories
            shutil.copy2(pathFile, '/home/chris/Pictures/test')




#print(extResults)
"""

zhdabuzwbvr21.jpg
Screenshot from 2019-04-05 15-45-21.png
z6ickpul15r21.jpg
Screenshot from 2019-04-05 15-45-02.png
Screenshot from 2019-04-05 15-44-51.png
dlk1s4by90331.jpg
Screenshot from 2019-04-01 19-18-41.png
a8g3xc0yhk821.jpg
selim_surgery_center_logoA_bevel2-280x164.png
Screenshot from 2019-04-05 15-45-05 - 1.png
c5eec78aebc5ef7e5e6e005dc10e0625ff45673e.png
Screenshot from 2019-04-05 15-45-32.png
Screenshot from 2019-04-04 14-30-45.png
czaqoqwicbr21.jpg
du6.jpg
YHwOakm.jpg
face_10.9.2014.png
5y1tslajv0e21.jpg
Screenshot from 2019-04-04 14-31-15.png
Screenshot from 2019-04-15 12-43-27.png
Screenshot from 2019-04-05 15-44-48.png
Screenshot from 2019-04-05 15-45-22.png
WWjtVFN.jpg
Screenshot from 2019-04-05 15-45-05.png
wvnmgbvu1wt11.jpg
Screenshot from 2019-04-05 15-45-00.png
Screenshot from 2019-04-05 15-45-33.png
Screenshot from 2019-04-04 14-31-47.png
Screenshot from 2019-04-01 19-19-08.png
Screenshot from 2019-04-05 15-45-31.png
a8g3xc0yhk821.jpg
VbmBwot.png
czaqoqwicbr21.jpg
du6.jpg
1491860899517.jpg
VbmBwot (copy).png
3.jpg
2.jpg
6.jpg
2019-05-07.jpg
5.jpg
4.jpg

"""