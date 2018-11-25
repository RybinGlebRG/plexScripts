import re
from animeRoutine import classAnalyzingGroup, classPossibleNumbers


class Analyzer:

    def __init__(self, files):
        self.currentHypothesis = -1
        self.possibleNumbersList = []
        self.analyzingGroupsList = []

        for item in files:
            self.possibleNumbersList.append(classPossibleNumbers.PossibleNumbers(item))
        # for list in self.possibleNumbersList:
        #     print(list.file.fileName)

    def findHypoteses(self):
        for item in self.possibleNumbersList:
            item.possibleNumbers = re.findall("\d+", item.file.fileName)
            # print(item.possibleNumbers)

    def getGroupIdByPath(self, path):
        for i in range(0, len(self.analyzingGroupsList)):
            if self.analyzingGroupsList[i].path == path:
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

    def checkConditionsForGroup(self, possibleNumbersList):
        fromOne = True
        differsByOne = True
        hypoteses = []
        for item in possibleNumbersList:
            #print(item.possibleNumbers)
            #print(self.currentHypothesis)
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

    def setFileNumber(self):
        self.findHypoteses()
        self.analyzeHypoteses()
        for item in self.possibleNumbersList:
            item.file.number = item.possibleNumbers[self.currentHypothesis]

