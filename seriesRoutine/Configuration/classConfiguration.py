from seriesRoutine.Configuration import ClassParser
import classFileOperations
import classLogger
import sys
import datetime


class Configuration:

    def __init__(self):
        self.keyValueList = {}

    def __eq__(self, other):
        if self.keyValueList != other.keyValueList:
            return False
        return True

    def __ne__(self, other):
        if self.keyValueList != other.keyValueList:
            return True
        return False

    def setValue(self, key, value):
        if value is None:
            self.keyValueList[key.upper()] = None
            return
        for item in value:
            if item is not None:
                break
            self.keyValueList[key.upper()] = None
            return
        self.keyValueList[key.upper()] = value

    def is_key_exists(self, key):
        if self.keyValueList.get(key.upper()) is not None:
            return True
        return False

    def fill(self, fileName):
        parser = ClassParser.Parser()
        dictionary = parser.parse(fileName)
        self.merge(dictionary)

    def merge(self, dictionary):
        for key, value in dictionary.items():
            self.keyValueList[key] = value

    def getValue(self, key):
        return self.keyValueList.get(key.upper())

    def isIncludes(self, key, testValue):
        value = self.getValue(key)
        if value is None:
            return False
        if testValue in value:
            return True
        return False

    def is_ready(self):
        if self.getValue("userConfigurationFile") is not None:
            return True
        return False

    def deleteForbiddenSymbolsFromValue(self, key):
        forbiddenSymbols = self.getValue("forbiddenSymbols")
        value = self.getValue(key)
        for i in range(0, len(value)):
            if value[i] in forbiddenSymbols:
                value = value[:i - 1] + value[:i + 1]

    def formatSeasonNumber(self):
        seasonNumber = self.getValue("seasonNumber")[0].lstrip("0")
        if int(seasonNumber) < 10:
            seasonNumber = "0" + seasonNumber
        if seasonNumber != self.getValue("seasonNumber")[0]:
            self.setValue("seasonNumber", seasonNumber)

    def getAllPairs(self):
        return self.keyValueList

    # def get_user_configuration(self,directory, fileName):
    #     foundDirectory = None
    #     foundFile = None
    #     for root, dirs, files in classFileOperations.FileOperations.walk(directory):
    #         for file in files:
    #             if file == fileName:
    #                 foundDirectory = root
    #                 foundFile = file
    #                 break
    #     return foundDirectory, foundFile

    def checkWatcherPath(self):
        if self.getValue("watcherPath") is None:
            path = classFileOperations.FileOperations.abspath(sys.argv[0])
            ldir = classFileOperations.FileOperations.dirname(path)
            self.setValue("watcherPath", [ldir])

    def log(self):
        logger = classLogger.Logger()
        directory = classFileOperations.FileOperations.dirname(classFileOperations.FileOperations.abspath(__file__))
        logger.writeLog(directory, "debug", "configurationMain:", "w+")
        items = self.getAllPairs()
        for item in items:
            logger.writeLog(directory, "debug", item.key + "=" + item.value)
        logger.writeLog(directory, "debug", "-----------------------------------")

    def print(self):
        print("-----------------------------------")
        print(datetime.datetime.now())
        print("-----------------------------------")
        print("Configuration:")
        items = self.getAllPairs()
        for item in items.items():
            print(item)
        print("-----------------------------------")

    def load(self, absolute_file_name):
        self.fill(absolute_file_name)
        self.checkWatcherPath()
        foundDirectory = None
        foundFile = None
        for root, dirs, files in classFileOperations.FileOperations.walk(self.getValue("watcherPath")[0]):
            for file in files:
                if file == self.getValue("configurationFileName")[0]:
                    foundDirectory = root
                    foundFile = file
                    break
        self.setValue("directoryPath", [foundDirectory])
        self.setValue("userConfigurationFile", [foundFile])
        if self.getValue("userConfigurationFile") is None:
            return
        self.fill(classFileOperations.FileOperations.join(self.getValue("directoryPath")[0],
                                                          self.getValue("userConfigurationFile")[0]))
        #self.print()
        self.deleteForbiddenSymbolsFromValue("titleName")
        self.formatSeasonNumber()

        classFileOperations.FileOperations.rename(
            classFileOperations.FileOperations.join(self.getValue("directoryPath")[0],
                                                    classFileOperations.FileOperations.join(
                                                        self.getValue("directoryPath")[0],
                                                        self.getValue(
                                                            "userConfigurationFile")[0])),
            classFileOperations.FileOperations.join(self.getValue("directoryPath")[0],
                                                    self.getValue("configurationFileNameUsed")[0]))
