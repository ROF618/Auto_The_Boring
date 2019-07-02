"""
Practice Projects

For practice, write programs to do the following tasks.
Selective Copy

DONE -> Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.
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
def copyFileExt(StartDirectory, EndDirectory, fileExt):
    #traverse the directory and subdirectories
    for folderName, subfolders, filenames in os.walk(str(StartDirectory)):
        #iterate over all of the files in the directories
        for file in filenames:
            #filter files with desired file extension
            if file.endswith(str(fileExt)):
                pathFile = os.path.join(folderName, file)
                try:
                    #copy the filtered files to new directory
                    shutil.copy2(pathFile, str(EndDirectory))
                #handles the same file shutil error and allows the program to continue
                except Exception as msg:
                    print(msg)
                    continue

#copyFileExt("/home/chris/Pictures", "/home/chris/Pictures/test", "png")


def findLargeFile(StartDirectory):
    for folderName, subFolders, fileNames in os.walk(str(StartDirectory)):
        for file in fileNames:
            try:
                pathFile = os.path.join(folderName, file)
                if os.path.getsize(pathFile) > 100:
                    print(os.path.abspath(file))

            except Exception as msg:
                print(msg)
                continue

#findLargeFile('/home/chris/Pictures')

def findPreFix(Direc):
    for file in os.scandir(Direc):
        print(file)

findPreFix('/home/chris/Pictures/')