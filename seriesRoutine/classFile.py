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
            # print(file_1.fileName)
            # print(repr(file_1.number))
            # print(repr(file_2.number))
            # print("8".rjust(2))
            equal = False
        if file_1.fileName != file_2.fileName:
            #print("9".rjust(2))
            equal = False
        if file_1.path != file_2.path:
            #print("10".rjust(2))
            equal = False
        if len(file_1.possibleSeriesNumbers) != len(file_2.possibleSeriesNumbers):
            #print("11".rjust(3))
            equal = False
        else:
            for i in range(0, len(file_1.possibleSeriesNumbers)):
                if file_1.possibleSeriesNumbers[i] != file_2.possibleSeriesNumbers[i]:
                    #print("12".rjust(3))
                    equal = False

        return equal
