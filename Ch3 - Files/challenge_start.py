import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile



def main():
    os.makedirs("Results")
    resultsFile = open("Results/results.txt", "w+")
    filelist = os.listdir()
    for file in filelist:
        if  os.path.isdir(file):
            continue
        else:
            resultsFile.write(file + "\n")
    resultsFile.close()
        










if __name__ == "__main__":
    main()
