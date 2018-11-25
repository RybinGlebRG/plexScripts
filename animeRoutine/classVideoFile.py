class VideoFile:

    def __init__(self, fileName, path):
        self.number = -1
        self.fileName = fileName
        self.path = path
        self.linkFileName = ""

    def getSuffix(self):
        lastDot = self.fileName.rfind(".")
        suffix = self.fileName[lastDot + 1:]
        return suffix