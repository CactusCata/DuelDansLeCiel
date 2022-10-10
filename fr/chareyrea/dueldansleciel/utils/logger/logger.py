import os
from datetime import datetime
import utils.debug as debug
import re
from zipfile import ZipFile
import shutil

LOG_FOLDER_NAME = "../../../logs"
last_folder_name_created = "0000_00_00-00:00:00"

class Logger:

    def __init__(self):
        if not os.path.exists(LOG_FOLDER_NAME):
            debug.l("Logger", "Trying to create logs folder")
            os.mkdir(LOG_FOLDER_NAME)
            debug.success("Logger", "logs folder successfully created")

    def createLogFolder(self):
        global last_folder_name_created

        fileName = datetime.now().strftime("%Y_%m_%d-%Hh%M")

        fileNameIterator = fileName
        count = 1
        while os.path.exists(LOG_FOLDER_NAME + '/' + fileNameIterator):
            fileNameIterator = fileName + '(' + str(count) + ')'
            count += 1


        os.mkdir(LOG_FOLDER_NAME + '/' + fileNameIterator)
        last_folder_name_created = fileNameIterator

    def zipAllOldLogs(self):

        fileDeleted = set()

        for fName in os.listdir(LOG_FOLDER_NAME):

            if bool(re.match("^\d{4}_\d{2}_\d{2}-\d{2}h\d{2}$", fName)):
                zipObj = ZipFile(fName + '.zip', 'w')
                self.zipAllFileInDir(zipObj, LOG_FOLDER_NAME + '/' + fName)
                zipObj.close()
                shutil.move(fName + '.zip', LOG_FOLDER_NAME + '/' + fName + '.zip')

                fileDeleted.add(LOG_FOLDER_NAME + '/' + fName)


        for fName in fileDeleted:
            shutil.rmtree(fName)

    def zipAllFileInDir(self, zipFile, path):
        for fName in os.listdir(path):
            if os.path.isdir(path + '/' + fName):
                self.zipAllFileInDir(zipFile, path + '/' + fName)
            else:
                zipFile.write(path + '/' + fName)
