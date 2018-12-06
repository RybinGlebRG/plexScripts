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
