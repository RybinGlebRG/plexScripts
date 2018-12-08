import re
from seriesRoutine.Analyzer import classAnalyzingGroup


class SeriesAnalyzer:

    def __init__(self):
        pass

    @staticmethod
    def findHypoteses(files):
        for file in files:
            file.possibleSeriesNumbers = re.findall("\d+", file.fileName)
            for i in range(0, len(file.possibleSeriesNumbers)):
                file.possibleSeriesNumbers[i] = file.possibleSeriesNumbers[i].lstrip("0")
                if file.possibleSeriesNumbers[i] == "":
                    file.possibleSeriesNumbers[i] = 0
                else:
                    file.possibleSeriesNumbers[i] = int(file.possibleSeriesNumbers[i])

    @staticmethod
    def getGroupIdByPath(analyzingGroupsList, path):
        for i in range(0, len(analyzingGroupsList)):
            if analyzingGroupsList[i].path == path:
                return i

    # Разбиваем общий список на подсписки на основе каталога расположения
    @staticmethod
    def divideByGroup(files):
        appended = []
        analyzingGroupsList = []
        for file in files:
            if file.path not in appended:
                appended.append(file.path)
                analyzingGroupsList.append(classAnalyzingGroup.AnalyzingGroup(file.path))
                analyzingGroupsList[
                    SeriesAnalyzer.getGroupIdByPath(analyzingGroupsList, file.path)].files.append(file)
            else:
                analyzingGroupsList[
                    SeriesAnalyzer.getGroupIdByPath(analyzingGroupsList, file.path)].files.append(file)
        return analyzingGroupsList

    @staticmethod
    def checkConditionsForGroup(group, currentHypothesis):
        fromOne = True
        fromZero = False
        isGrowing = True
        hypoteses = []
        for file in group.files:
            if file.number is not None:
                hypoteses.append(file.number)
            else:
                #print(file.possibleSeriesNumbers[currentHypothesis])
                hypoteses.append(file.possibleSeriesNumbers[currentHypothesis])
        hypoteses.sort()
        # print(hypoteses)
        if hypoteses[0] != 1:
            fromOne = False

        if hypoteses[0] == 0:
            fromZero = True

        # print(len(hypoteses))
        for i in range(1, len(hypoteses)):
            previous = hypoteses[i - 1]
            # if previous == 0:
            #     previous = 0
            # else:
            #     previous = int(previous)
            current = hypoteses[i]

            if current <= previous:
                isGrowing = False

        # print(differsByOne)
        # print(fromOne)
        # print(fromZero)
        if (fromOne or fromZero) and isGrowing:
            return True
        else:
            return False

    @staticmethod
    def analyzeHypoteses(files, groups):
        # self.divideByGroup(files)
        # groups=self.analyzingGroupsList
        currentHypothesis = None
        for group in groups:
            # print("------------------------")
            # print(group.path)
            # Полагаем, что в группе файлов все файлы, которые отличаются только номером серии
            # имеют номер серии, равный None. Файлы, отличающиеся от основных должны быть явно
            # прописаны в пользовательской конфигурации и на данный момент уже иметь номер серии
            length = None
            for file in group.files:
                # print(file.fileName)
                if file.number is None:
                    length = len(file.possibleSeriesNumbers)
                    break
            for i in range(0, length):
                currentHypothesis = i
                conditionsMet = SeriesAnalyzer.checkConditionsForGroup(group, currentHypothesis)
                # print("--------------------------")
                # print(currentHypothesis)
                # print(conditionsMet)
                if conditionsMet:
                    group.hypothesis = currentHypothesis
                    break

    @staticmethod
    def setFileNumber(files):
        SeriesAnalyzer.findHypoteses(files)

        groups = SeriesAnalyzer.divideByGroup(files)
        SeriesAnalyzer.analyzeHypoteses(files, groups)

        for group in groups:
            for file in group.files:
                if file.number is None:
                    file.number=file.possibleSeriesNumbers[group.hypothesis]

