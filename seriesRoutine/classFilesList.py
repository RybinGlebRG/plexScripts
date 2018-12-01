class FilesList:

    def __init__(self, configuration):
        self.filesList = []
        self.configuration = configuration

    def append(self, file):
        self.filesList.append(file)

    def filterVideoFiles(self):
        videoFilesList = []
        for file in self.filesList:
            if self.configuration.isIncludes("videoFileSuffixes", file.getSuffix()):
                videoFilesList.append(file)
        return videoFilesList

    def filterAudioFiles(self):
        audioFilesList = []
        for file in self.filesList:
            if self.configuration.isIncludes("audioFileSuffixes", file.getSuffix()):
                audioFilesList.append(file)
        return audioFilesList

    def filterSubsFiles(self):
        subsFilesList = []
        for file in self.filesList:
            if self.configuration.isIncludes("subsFileSuffixes", file.getSuffix()):
                subsFilesList.append(file)
        return subsFilesList

    def filterImageFiles(self):
        imageFilesList = []
        for file in self.filesList:
            if self.configuration.isIncludes("imageFileSuffixes", file.getSuffix()):
                imageFilesList.append(file)
        return imageFilesList
