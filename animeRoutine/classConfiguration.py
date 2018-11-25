from animeRoutine import classKeyValue
import io
import classFileOperations
import classLogger


class Configuration:

    def __init__(self):
        self.keyValueList = []
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
                key = ""
            return key.strip()

        def getValueFromString(line):
            def isMultipleValues(value):
                position = value.find(";")
                if position == -1:
                    return False
                else:
                    return True

            value = ""
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
            return value

        # lines = [line   .strip() for line in open(fileName)]
        lines = []
        # for line in io.open(fileName,encoding="utf-8"):
        # for line in classFileOperations.FileOperations.open(fileName):
        #     lines.append(line)

        lines = classFileOperations.FileOperations.readFile(fileName)

        for line in lines:
            if line[0] != "#":
                if getKeyFromString(line) != "":
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
