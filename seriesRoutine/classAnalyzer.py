import re
from seriesRoutine import classAnalyzingGroup, classPossibleNumbers
from seriesRoutine import classFile
from seriesRoutine import classAnalyzingGroup_v2


class Analyzer:

    def __init__(self, files):
        self.currentHypothesis = -1
        self.possibleNumbersList = []
        self.analyzingGroupsList = []
        self.analyzingGroupsList_v2 = []
        self.files = files
        self.currentHypothesis_v2 = -1

        for item in self.files:
            self.possibleNumbersList.append(classPossibleNumbers.PossibleNumbers(item))
            # item.possibleSeriesNumbers = classPossibleNumbers.PossibleNumbers(item).possibleNumbers
        # for list in self.possibleNumbersList:
        #     print(list.file.fileName)

    def findHypoteses(self):
        for item in self.possibleNumbersList:
            item.possibleNumbers = re.findall("\d+", item.file.fileName)
        for file in self.files:
            file.possibleSeriesNumbers = re.findall("\d+", file.fileName)
            # print(item.possibleNumbers)

    def getGroupIdByPath(self, path):
        for i in range(0, len(self.analyzingGroupsList)):
            if self.analyzingGroupsList[i].path == path:
                return i

    def getGroupIdByPath_v2(self, analyzingGroupsList, path):
        for i in range(0, len(analyzingGroupsList)):
            if analyzingGroupsList[i].path == path:
                return i

    # Разбиваем общий список на подсписки на основе каталога расположения
    def divideByGroup(self):
        self.analyzingGroupsList = []
        appended = []
        for item in self.possibleNumbersList:
            if item.file.path not in appended:
                appended.append(item.file.path)
                self.analyzingGroupsList.append(classAnalyzingGroup.AnalyzingGroup(item.file.path))
                self.analyzingGroupsList[self.getGroupIdByPath(item.file.path)].possibleNumbersList.append(item)
            else:
                self.analyzingGroupsList[self.getGroupIdByPath(item.file.path)].possibleNumbersList.append(item)

        appended_v2 = []
        for file in self.files:
            if file.path not in appended_v2:
                appended_v2.append(file.path)
                self.analyzingGroupsList_v2.append(classAnalyzingGroup_v2.AnalyzingGroup(file.path))
                self.analyzingGroupsList_v2[
                    self.getGroupIdByPath_v2(self.analyzingGroupsList_v2, file.path)].files.append(file)
            else:
                self.analyzingGroupsList_v2[
                    self.getGroupIdByPath_v2(self.analyzingGroupsList_v2, file.path)].files.append(file)

    def checkConditionsForGroup(self, possibleNumbersList):
        fromOne = True
        differsByOne = True
        hypoteses = []
        for item in possibleNumbersList:
            # print(item.possibleNumbers)
            # print(self.currentHypothesis)
            hypoteses.append(item.possibleNumbers[self.currentHypothesis])
        hypoteses.sort()
        if hypoteses[0].lstrip("0") != "1":
            fromOne = False

        for i in range(1, len(hypoteses)):
            if (int(hypoteses[i].lstrip("0")) - int(hypoteses[i - 1].lstrip("0"))) != 1:
                differsByOne = False
        if fromOne and differsByOne:
            return True
        else:
            return False

    def checkConditionsForGroup_v2(self, group, currentHypothesis):
        fromOne = True
        fromZero = False
        differsByOne = True
        hypoteses = []
        # for item in possibleNumbersList:
        #     # print(item.possibleNumbers)
        #     # print(self.currentHypothesis)
        #     hypoteses.append(item.possibleNumbers[currentHypothesis])
        for file in group.files:
            hypoteses.append(file.possibleSeriesNumbers[currentHypothesis])
        hypoteses.sort()
        if hypoteses[0].lstrip("0") != "1":
            fromOne = False

        if hypoteses[0].lstrip("0") == "":
            fromZero = True

        for i in range(1, len(hypoteses)):
            previous=hypoteses[i-1].lstrip("0")
            if previous=="":
                previous=0
            else:
                previous=int(previous)
            current=int(hypoteses[i].lstrip("0"))

            for i in range(1, len(hypoteses)):
                if (current-previous) != 1:
                    differsByOne = False
        if (fromOne or fromZero)and differsByOne:
            return True
        else:
            return False

    def analyzeHypoteses(self):
        self.divideByGroup()
        for group in self.analyzingGroupsList:
            # TODO: Получение длины нужно переписать
            length = len(group.possibleNumbersList[0].possibleNumbers)
            self.currentHypothesis = -1
            for i in range(0, length):
                self.currentHypothesis += 1
                conditionsMet = self.checkConditionsForGroup(group.possibleNumbersList)
                if conditionsMet:
                    break

        for group in self.analyzingGroupsList_v2:
            # TODO: Получение длины нужно переписать
            length = len(group.files[0].possibleSeriesNumbers)
            for i in range(0, length):
                self.currentHypothesis_v2 = i
                conditionsMet = self.checkConditionsForGroup_v2(group, self.currentHypothesis_v2)
                if conditionsMet:
                    break
            group.hypothesis=self.currentHypothesis_v2

    def setFileNumber(self):
        self.findHypoteses()
        self.analyzeHypoteses()
        # for item in self.possibleNumbersList:
        #     item.file.number = item.possibleNumbers[self.currentHypothesis]
        for group in self.analyzingGroupsList_v2:
            max_number=-1
            for file in group.files:
                if file.possibleSeriesNumbers[group.hypothesis]>max_number:
                    max_number=file.possibleSeriesNumbers[group.hypothesis]
            for file in group.files:
                file.number=file.possibleSeriesNumbers[group.hypothesis].lstrip("0").zfill(len(str(max_number)))
