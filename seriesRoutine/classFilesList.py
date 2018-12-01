class FilesList:

    def __init__(self, configuration):
        self.filesList = []
        self.configuration = configuration
        self.test_data = []

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

    def add_test_data(self, file):
        self.test_data.append(file)

    def test(self):
        print("Files:")
        passed = True
        for file in self.test_data:
            found = False
            for item in self.filesList:
                if file.fileName == item.fileName and file.path == item.path:
                    found = True
                    if file.number != item.number:
                        passed = False
                    if file.linkFileName != item.linkFileName:
                        passed = False
                    if len(file.possibleSeriesNumbers) != len(item.possibleSeriesNumbers):
                        passed = False
                    for i in range(0, len(file.possibleSeriesNumbers)):
                        if file.possibleSeriesNumbers[i] != item.possibleSeriesNumbers[i]:
                            passed = False
            passed = found and passed
        if passed:
            print("Passed")
        else:
            print("Failed")
