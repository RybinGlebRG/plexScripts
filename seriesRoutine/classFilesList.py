class FilesList:

    def __init__(self, configuration):
        self.filesList = []
        self.configuration = configuration
        self.test_data = []

    def get_list(self):
        return self.filesList

    def add(self, file):
        self.filesList.append(file)

    def filterVideoFiles(self):
        videoFilesList=FilesList(self.configuration)
        videoFiles = []
        for file in self.filesList:
            if self.configuration.isIncludes("videoFileSuffixes", file.getSuffix()):
                videoFiles.append(file)
                videoFilesList.add(file)
        return videoFilesList

    def filterAudioFiles(self):
        audioFilesList=FilesList(self.configuration)
        audioFiles = []
        for file in self.filesList:
            if self.configuration.isIncludes("audioFileSuffixes", file.getSuffix()):
                audioFiles.append(file)
                audioFilesList.add(file)
        return audioFilesList

    def filterSubsFiles(self):
        subs_files_list=FilesList(self.configuration)
        subsFiles = []
        for file in self.filesList:
            if self.configuration.isIncludes("subsFileSuffixes", file.getSuffix()):
                subsFiles.append(file)
                subs_files_list.add(file)
        return subs_files_list

    def filterImageFiles(self):
        image_files_list=FilesList(self.configuration)
        imageFiles = []
        for file in self.filesList:
            if self.configuration.isIncludes("imageFileSuffixes", file.getSuffix()):
                imageFiles.append(file)
                image_files_list.add(file)
        return image_files_list

    def add_test_data(self, file):
        self.test_data.append(file)

    def test(self):
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
        self.test_data = []
        return passed
