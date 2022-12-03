# GOAL: Open every folder within a directory and then sort the files I want into diffrent folders that are named by file ending

import os
import shutil


# By Greenwavemonster :)

def userIn():  # Get the Paths + Validation
    global startDir
    global endDir   #YEEEES I knowwwww don't make global vars
    global fileEnd

    print("Enter full Path to Dir from which you want to extract files (C:\\Users\\Greenwave\\FolderX\\FolderY): ")
    while True:
        startDir = input()  # Back then I didn't know try:exept was a thing ;) too lazy to redo
        if os.path.exists(startDir):
            print("Enter the full Path to where you want the files to be (C:\\Users\\Greenwave\\destination): ")
            while True:
                endDir = input()
                if os.path.exists(endDir):
                    print("Sorting: HTML, PNG, JPG etc.: ")
                    break
                print("Seems not like a valid Destination... Try again: ")
            break
        print("Not a valid Path... Try again: ")


def discFiles():
    files = os.scandir(startDir)
    print("Sorting... ")
    for entry in files:
        path1 = startDir + "\\" + str(entry.name) + "\\"
        print(path1)
        subscan = os.scandir(path1)
        for file in subscan:
            name = file.name
            path2 = path1 + name
            ending = os.path.splitext(name)
            match ending[1]:

                # IMAGES
                case ".png":
                    moveFile(ending, name, path2)
                case ".jpg":
                    moveFile(ending, name, path2)
                case ".jpeg":
                    moveFile(ending, name, path2)
                case ".svg":
                    moveFile(ending, name, path2)
                case ".tif":
                    moveFile(ending, name, path2)
                case ".heic":
                    moveFile(ending, name, path2)

                # MOVIES
                case ".mp4":
                    moveFile(ending, name, path2)
                case ".mov":
                    moveFile(ending, name, path2)

                # SOUND
                case ".mp3":
                    moveFile(ending, name, path2)
                case ".caf":
                    moveFile(ending, name, path2)

                # SCRIPTS
                case ".py":
                    moveFile(ending, name, path2)
                case ".java":
                    moveFile(ending, name, path2)
                case ".sqlite":
                    moveFile(ending, name, path2)

                # DOCUMENTS
                case ".txt":
                    moveFile(ending, name, path2)
                case ".pdf":
                    moveFile(ending, name, path2)
                case ".docx":
                    moveFile(ending, name, path2)
                case ".rtf":
                    moveFile(ending, name, path2)
                case ".xlsx":
                    moveFile(ending, name, path2)

                # WEBSITES
                case ".html":
                    moveFile(ending, name, path2)
                case ".webp":
                    moveFile(ending, name, path2)

                # COMPRESSIONS
                case ".gz":
                    moveFile(ending, name, path2)
                case ".zip":
                    moveFile(ending, name, path2)
                case ".rar":
                    moveFile(ending, name, path2)
                case ".tar":
                    moveFile(ending, name, path2)

                # DEFAULT
                case default:
                    print("default")


def moveFile(ending, name, path2):
    e = ending[1]
    folder = e[1:]
    folderPath = os.path.join(endDir, folder)
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    else:
        pass

    try:
        shutil.move(path2, folderPath)
    except FileExistsError:
        pass

    print("File " + str(name) + " has been Moved to: " + folder)


# === START ===
print("=== Start ===")
userIn()
discFiles()
print("=== Done ===")

