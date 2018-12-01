from seriesRoutine import classKeyValue
import io
import classFileOperations
import classLogger
import sys


class Configuration:

    def __init__(self):
        self.keyValueList = []
        self.test_data = []
        # self.keyValueList.append(classKeyValue.KeyValue("videoFileSuffixes", ["mkv"]))
        # self.keyValueList.append(classKeyValue.KeyValue("audioFileSuffixes", ["ac3"]))
        # self.keyValueList.append(classKeyValue.KeyValue("subsFileSuffixes", ["ass"]))
        # self.keyValueList.append(classKeyValue.KeyValue("titleName"))
        # self.keyValueList.append(classKeyValue.KeyValue("seasonNumber"))
        # self.keyValueList.append(classKeyValue.KeyValue("sourcePath"))
        # self.keyValueList.append(classKeyValue.KeyValue("targetPath"))

    def createKey(self, key, value=""):
        self.keyValueList.append(classKeyValue.KeyValue(key, value))

    def setValue(self, key, value):
        for i in range(0, len(self.keyValueList)):
            if self.keyValueList[i].key.upper() == key.upper():
                self.keyValueList[i].value = value
                break

    def isKeyExists(self, key):
        isExists = False
        for item in self.keyValueList:
            if item.key.upper() == key.upper():
                isExists = True
                break
        return isExists

    def load(self, fileName):
        # print(fileName)
        def getKeyFromString(line):
            key = ""
            foundDelimeter = False
            for letter in line:
                if letter != "=":
                    key += letter
                else:
                    foundDelimeter = True
                    break
            if not foundDelimeter:
                key = None
            return key.strip()

        def getValueFromString(line):
            def isMultipleValues(value):
                position = value.find(";")
                if position == -1:
                    return False
                else:
                    return True

            value = None
            delimiter = line.find("=")

            if delimiter != -1:
                if not isMultipleValues(line[(delimiter + 1):]):
                    value = line[(delimiter + 1):]
                    value = value.strip()
                else:
                    value = line[(delimiter + 1):]
                    value = value.split(";")
                    for i in range(0, len(value)):
                        value[i] = value[i].strip()
                if len(value) == 0:
                    value = None
            return value

        # lines = [line   .strip() for line in open(fileName)]
        # lines = []
        # for line in io.open(fileName,encoding="utf-8"):
        # for line in classFileOperations.FileOperations.open(fileName):
        #     lines.append(line)

        lines = classFileOperations.FileOperations.readFile(fileName)

        for line in lines:
            # print(line)
            if line[0] != "#":
                if getKeyFromString(line) is not None:
                    if self.isKeyExists(getKeyFromString(line)):
                        # print(getValueFromString(line))
                        self.setValue(getKeyFromString(line), getValueFromString(line))
                    else:
                        # print(getValueFromString(line))
                        self.createKey(getKeyFromString(line), getValueFromString(line))

    def getValue(self, key):
        for item in self.keyValueList:
            if item.key.upper() == key.upper():
                return item.value

    def getValueAsList(self, key):
        for item in self.keyValueList:
            if item.key.upper() == key.upper():
                if isinstance(item.value, str):
                    return [item.value]
                if isinstance(item.value, list):
                    return item.value

    def isIncludes(self, key, testValue):
        value = self.getValue(key)
        if isinstance(value, str):
            if value.upper() == testValue.upper():
                return True
            else:
                return False
        if isinstance(value, list):
            if testValue in value:
                return True
            else:
                return False

    def deleteForbiddenSymbolsFromValue(self, key):
        forbiddenSymbols = self.getValue("forbiddenSymbols")
        value = self.getValue(key)
        for i in range(0, len(value)):
            if value[i] in forbiddenSymbols:
                value = value[:i - 1] + value[:i + 1]

    def formatSeasonNumber(self):
        seasonNumber = self.getValue("seasonNumber").lstrip("0")
        if int(seasonNumber) < 10:
            seasonNumber = "0" + seasonNumber
        if seasonNumber != self.getValue("seasonNumber"):
            self.setValue("seasonNumber", seasonNumber)

    def getAllPairs(self):
        items = []
        for pair in self.keyValueList:
            temp = None

            if isinstance(pair.value, list):
                temp = str(pair.value)
            else:
                temp = pair.value
            item = classKeyValue.KeyValue(pair.key, temp)
            items.append(item)
        return items

    @staticmethod
    def findUserConfigurationFile(directory, fileName):
        foundDirectory = ""
        foundFile = ""
        for root, dirs, files in classFileOperations.FileOperations.walk(directory):
            # print(files)
            for file in files:
                # print(classFileOperations.FileOperations.join(root, file))
                # print(classFileOperations.FileOperations.join(root, fileName))
                # print(file)
                # print(fileName)
                if file == fileName:
                    # print("LOL")
                    foundDirectory = root
                    foundFile = file
                    break
        return foundDirectory, foundFile

    def checkWatcherPath(self):
        if self.getValue("watcherPath") is None:
            path = classFileOperations.FileOperations.abspath(sys.argv[0])
            ldir = classFileOperations.FileOperations.dirname(path)
            self.setValue("watcherPath", ldir)

    def addTestData(self, key, value=""):
        self.test_data.append(classKeyValue.KeyValue(key, value))

    def test(self):
        print("Configuration:")
        passed = True
        for pair in self.test_data:
            # print("------------------------------")
            # print(repr(pair.key))
            # print("")
            keyExist = True
            valueOK = True
            for item in self.keyValueList:
                # print(repr(item.key))
                # print(pair.key==item.key)
                if item.key == pair.key:
                    # print(item.key+" = "+str(item.value))
                    # print(pair.key+" = "+str(pair.value))
                    # print("---------------------------------")
                    # keyExist = True
                    if isinstance(pair.value, list):
                        if len(pair.value) != len(item.value):
                            valueOK = False
                        else:
                            valueOK = valueOK and True
                        for i in range(0, len(pair.value)):
                            if pair.value[i] != item.value[i]:
                                valueOK = False
                                break
                            else:
                                valueOK = valueOK and True

                    else:
                        if item.value == pair.value:
                            valueOK = True
            if not keyExist or not valueOK:
                print(pair.key)
                passed = False
                # return False
        fileOld = None
        fileNew = None
        for item in self.keyValueList:
            if item.key == "directoryPath":
                fileOld = classFileOperations.FileOperations.join(item.value, "configuration.ready")
                fileNew = classFileOperations.FileOperations.join(item.value, "configuration.txt")
        if classFileOperations.FileOperations.exists(fileOld):
            passed = False
            # return False
        if not classFileOperations.FileOperations.exists(fileNew):
            passed = False
            # return False
        self.test_data = []
        if not passed:
            print("Failed")
            return None
        else:
            print("Passed")
