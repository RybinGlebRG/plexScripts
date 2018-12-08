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

    def __eq__(self, other):
        if self.number != other.number:
            return False
        if self.fileName != other.fileName:
            return False
        if self.path != other.path:
            return False
        if self.possibleSeriesNumbers != other.possibleSeriesNumbers:
            return False
        return True

    def __ne__(self, other):
        if self.number != other.number:
            return True
        if self.fileName != other.fileName:
            return True
        if self.path != other.path:
            return True
        if self.possibleSeriesNumbers != other.possibleSeriesNumbers:
            return True
        return False

    def check_specified(self, configuration):
        if configuration is not None:
            if configuration.isIncludes("addFile", self.fileName):
                addFiles = configuration.getValue("addFile")
                i = addFiles.index(self.fileName)
                self.number = configuration.getValue("addFileNumber")[i].lstrip("0")
                if self.number == "":
                    self.number = "0"
                    self.number = int(self.number)

    def copy(self):
        file = File(self.fileName, self.path)
        file.number = self.number
        file.linkFileName = self.linkFileName
        file.possibleSeriesNumbers = self.possibleSeriesNumbers.copy()
        return file
