class File:

    def __init__(self, fileName, path):
        self.number = None
        self.fileName = fileName
        self.path = path
        self.linkFileName = None
        self.possibleSeriesNumbers=[]

    def getSuffix(self):
        lastDot = self.fileName.rfind(".")
        suffix = self.fileName[lastDot + 1:]
        return suffix
