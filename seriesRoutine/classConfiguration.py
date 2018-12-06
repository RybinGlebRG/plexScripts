from seriesRoutine import classKeyValue, ClassParser
import classFileOperations
import classLogger
import sys


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
        if not isinstance(value, list):
            self.keyValueList[key.upper()] = list(value)
        self.keyValueList[key.upper()] = value

    def is_key_exists(self, key):
        if self.keyValueList.get(key.upper()) is not None:
            return True
        return False

    def load(self, fileName):
        parser = ClassParser.Parser()
        self.keyValueList = parser.parse(fileName)

    def getValue(self, key):
        return self.keyValueList.get(key.upper())

    def isIncludes(self, key, testValue):
        value = self.getValue(key)
        if value is None:
            return False
        if testValue in value:
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

    @staticmethod
    def findUserConfigurationFile(directory, fileName):
        foundDirectory = ""
        foundFile = ""
        for root, dirs, files in classFileOperations.FileOperations.walk(directory):
            for file in files:
                if file == fileName:
                    foundDirectory = root
                    foundFile = file
                    break
        return foundDirectory, foundFile

    def checkWatcherPath(self):
        if self.getValue("watcherPath") is None:
            path = classFileOperations.FileOperations.abspath(sys.argv[0])
            ldir = classFileOperations.FileOperations.dirname(path)
            self.setValue("watcherPath", ldir)

    def log(self):
        logger = classLogger.Logger()
        directory = classFileOperations.FileOperations.dirname(classFileOperations.FileOperations.abspath(__file__))
        logger.writeLog(directory, "debug", "configurationMain:", "w+")
        items = self.getAllPairs()
        for item in items:
            logger.writeLog(directory, "debug", item.key + "=" + item.value)
        logger.writeLog(directory, "debug", "-----------------------------------")
