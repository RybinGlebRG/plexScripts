import re
from seriesRoutine import classAnalyzingGroup


class SeriesAnalyzer:

    def __init__(self):
        pass
        # self.analyzingGroupsList = []
        # self.files = files
        # self.currentHypothesis = -1

    @staticmethod
    def findHypoteses(files):
        for file in files:
            file.possibleSeriesNumbers = re.findall("\d+", file.fileName)

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
                hypoteses.append(file.possibleSeriesNumbers[currentHypothesis])
        hypoteses.sort()
        # print(hypoteses)
        if hypoteses[0].lstrip("0") != "1":
            fromOne = False

        if hypoteses[0].lstrip("0") == "":
            fromZero = True

        # print(len(hypoteses))
        for i in range(1, len(hypoteses)):
            previous = hypoteses[i - 1].lstrip("0")
            if previous == "":
                previous = 0
            else:
                previous = int(previous)
            current = int(hypoteses[i].lstrip("0"))

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
            # TODO: Получение длины нужно переписать
            # Полагаем, что в группе файлов все файлы, которые отличаются только номером серии
            # имеют номер серии, равный None. Файлы, отличающиеся от основных должны быть явно
            # прописаны в пользовательской конфигурации и на данный момент уже иметь номер серии
            length = None
            for file in group.files:
                if file.number is None:
                    length = len(file.possibleSeriesNumbers)
            for i in range(0, length):
                currentHypothesis = i
                conditionsMet = SeriesAnalyzer.checkConditionsForGroup(group, currentHypothesis)
                if conditionsMet:
                    break
            group.hypothesis = currentHypothesis

    @staticmethod
    def setFileNumber(files):
        SeriesAnalyzer.findHypoteses(files)
        groups = SeriesAnalyzer.divideByGroup(files)
        SeriesAnalyzer.analyzeHypoteses(files, groups)

        for group in groups:
            max_number = 0
            for file in group.files:
                if file.number is not None:
                    cur_num=file.number.lstrip("0")
                else:
                    cur_num = file.possibleSeriesNumbers[group.hypothesis].lstrip("0")
                if cur_num == "":
                    cur_num = 0
                else:
                    cur_num = int(cur_num)
                max_number = (str(max_number)).lstrip("0")
                if max_number == "":
                    max_number = 0
                else:
                    max_number = int(max_number)
                if cur_num > max_number:
                    max_number = cur_num
            for file in group.files:
                if file.number is not None:
                    file.number=file.number.lstrip("0").zfill(len(str(max_number)))
                else:
                    file.number = file.possibleSeriesNumbers[group.hypothesis].lstrip("0").zfill(len(str(max_number)))
