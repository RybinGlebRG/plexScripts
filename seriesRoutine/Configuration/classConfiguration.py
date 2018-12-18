from seriesRoutine.Configuration import ClassParser
from common import classFileOperations
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
        return self.keyValueList.items()

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
        # logger = classLogger.Logger()
        # directory = classFileOperations.FileOperations.dirname(classFileOperations.FileOperations.abspath(__file__))
        lines = []
        lines.append("configurationMain:")
        items = self.getAllPairs()
        for key, value in items:
            lines.append(key + "=" + str(value))
        lines.append("-----------------------------------")
        return lines

    def print(self):
        print("-----------------------------------")
        print(datetime.datetime.now())
        print("-----------------------------------")
        print("Configuration:")
        items = self.getAllPairs()
        for key, value in items:
            print(key + "=" + str(value))
        print("-----------------------------------")

    def left_add_to_path(self, key, add_value):
        values = self.getValue(key)
        if values is None:
            return
        result = []
        for value in values:
            if value is not None:
                new_value = classFileOperations.FileOperations.join(add_value, value)
                result.append(new_value)
        self.setValue(key, result)

    def load(self, absolute_file_name):
        # Fill with base configuration
        self.fill(absolute_file_name)
        self.checkWatcherPath()

        # Find user configuration file
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

        # If not found user configuration file
        if self.getValue("userConfigurationFile") is None:
            return

        # Fill with user configuration
        self.fill(classFileOperations.FileOperations.join(self.getValue("directoryPath")[0],
                                                          self.getValue("userConfigurationFile")[0]))
        self.deleteForbiddenSymbolsFromValue("titleName")
        #self.formatSeasonNumber()

        # Rename user configuration file to highlight its usage
        classFileOperations.FileOperations.rename(
            classFileOperations.FileOperations.join(self.getValue("directoryPath")[0],
                                                    classFileOperations.FileOperations.join(
                                                        self.getValue("directoryPath")[0],
                                                        self.getValue(
                                                            "userConfigurationFile")[0])),
            classFileOperations.FileOperations.join(self.getValue("directoryPath")[0],
                                                    self.getValue("configurationFileNameUsed")[0]))

        # TODO: Following cannot work with multiple source directories
        # Find video source directory
        sourcePath=self.getValue("source_path")
        if sourcePath is None:
            folders = []
            for folderList in classFileOperations.FileOperations.walk(self.getValue("directoryPath")[0]):
                folders = folderList[1]
                break
            sourcePath = self.getValue("directoryPath")[0]
            for folder in folders:
                if self.isIncludes("sourcePossibleLocation", folder):
                    sourcePath = classFileOperations.FileOperations.join(self.getValue("directoryPath")[0], folder)
                    # Is Lang needed (Do we have a container?)
                    if self.getValue("linkAudio")[0] == "A":
                        self.setValue("linkAudio", "N")
                    if self.getValue("linkSubs")[0] == "A":
                        self.setValue("linkSubs", "N")
                    break
            self.setValue("source_path", [sourcePath])
        else:
            self.left_add_to_path("source_path",self.getValue("directoryPath")[0])

        # Set Lang source directory full path
        self.left_add_to_path("lang_path", self.getValue("directoryPath")[0])
