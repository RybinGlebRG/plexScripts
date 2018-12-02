class File:

    def __init__(self, fileName, path):
        self.number = None
        self.fileName = fileName
        self.path = path
        self.linkFileName = None
        self.possibleSeriesNumbers = []

    def getSuffix(self):
        lastDot = self.fileName.rfind(".")
        suffix = self.fileName[lastDot + 1:]
        return suffix

    @staticmethod
    def are_equal(file_1, file_2):
        equal = True

        if file_1.number != file_2.number:
            equal = False
        if file_1.fileName != file_2.fileName:
            equal = False
        if file_1.path != file_2.path:
            equal = False
        if len(file_1.possibleSeriesNumbers) != len(file_2.possibleSeriesNumbers):
            equal = False
        else:
            for i in range(0, len(file_1.possibleSeriesNumbers)):
                if file_1.possibleSeriesNumbers[i] != file_2.possibleSeriesNumbers[i]:
                    equal = False

        return equal
