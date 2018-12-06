class FilesList:

    def __init__(self):
        self.filesList = []
        # self.configuration = None
        # self.test_data = []

    def __eq__(self, other):
        if self.filesList != other.filesList:
            return False
        # if self.configuration != other.configuration:
        #     return False
        return True

    def __ne__(self, other):
        if self.filesList != other.filesList:
            return True
        # if self.configuration != other.configuration:
        #     return True
        return False

    def __getitem__(self, key):
        return self.filesList[key]

    def get_list(self):
        return self.filesList

    def add(self, file):
        self.filesList.append(file)

    # def filterVideoFiles(self):
    #     videoFilesList = FilesList()
    #     videoFiles = []
    #     for file in self.filesList:
    #         if self.configuration.isIncludes("videoFileSuffixes", file.getSuffix()):
    #             videoFiles.append(file)
    #             videoFilesList.add(file)
    #     return videoFilesList
    #
    # def filterAudioFiles(self):
    #     audioFilesList = FilesList(self.configuration)
    #     audioFiles = []
    #     for file in self.filesList:
    #         if self.configuration.isIncludes("audioFileSuffixes", file.getSuffix()):
    #             audioFiles.append(file)
    #             audioFilesList.add(file)
    #     return audioFilesList
    #
    # def filterSubsFiles(self):
    #     subs_files_list = FilesList(self.configuration)
    #     subsFiles = []
    #     for file in self.filesList:
    #         if self.configuration.isIncludes("subsFileSuffixes", file.getSuffix()):
    #             subsFiles.append(file)
    #             subs_files_list.add(file)
    #     return subs_files_list
    #
    # def filterImageFiles(self):
    #     image_files_list = FilesList(self.configuration)
    #     imageFiles = []
    #     for file in self.filesList:
    #         if self.configuration.isIncludes("imageFileSuffixes", file.getSuffix()):
    #             imageFiles.append(file)
    #             image_files_list.add(file)
    #     return image_files_list

    def filter_by_number(self, number):
        filtered = FilesList()
        for file in self.filesList:
            if file.number == number:
                filtered.add(file)
        return filtered

    def filter_by_suffixes(self, suffixes):
        filtered = FilesList()
        for file in self.filesList:
            if file.getSuffix() in suffixes:
                filtered.add(file)
        return filtered
