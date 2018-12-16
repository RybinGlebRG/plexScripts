class Factory:

    def __init__(self, configuration):
        pass
        # self.configuration = configuration

    # @staticmethod
    # def checkIfSpecified(file, configuration):
    #     if configuration.isIncludes("addFile", file.fileName):
    #         addFiles = configuration.getValue("addFile")
    #         # for i in range(0, len(addFiles)):
    #         #     if addFiles[i] == file.fileName:
    #         #         file.number = configuration.getValueAsList("addFileNumber")[i].lstrip("")
    #         #         if file.number == "":
    #         #             file.number = "0"
    #         #
    #         #         file.number = int(file.number)
    #         i = addFiles.index(file.fileName)
    #         file.number = configuration.getValue("addFileNumber")[i].lstrip("0")
    #         if file.number == "":
    #             file.number = "0"
    #         file.number = int(file.number)

    # @staticmethod
    # def createFile(fileName, path, configuration=None):
    #     file = classFile.File(fileName, path)
    #     if configuration is not None:
    #         Factory.checkIfSpecified(file, configuration)
    #     return file

    # @staticmethod
    # def copyFile(file):
    #     #newFile = Factory.createFile(file.fileName, file.path)
    #     newFile = classFile.File(file.fileName, file.path)
    #     newFile.number = file.number
    #     newFile.possibleSeriesNumbers = file.possibleSeriesNumbers
    #     newFile.link_target = file.link_target
    #     return newFile

    # @staticmethod
    # def createEpisode(videoFile, subsFiles, audioFiles, imageFile):
    #     episode = classEpisode.Episode(videoFile.number)
    #     episode.video_files = videoFile
    #     episode.subs_files = subsFiles
    #     episode.audio_files = audioFiles
    #     episode.image_files = imageFile
    #     return episode

    # @staticmethod
    # def createEpisodesList(videoFiles, subsFiles, audioFiles, imageFiles, configuration):
    #     episodes_list = ClassEpisodesList.EpisodesList()
    #     for videoFile in videoFiles:
    #         suitable_subs_files = None
    #         if configuration.getValue("linkSubs")[0] != "N":
    #             suitable_subs_files = subsFiles.filter_by_number(videoFile.number)
    #
    #         suitable_audio_files = None
    #         if configuration.getValue("linkAudio")[0] != "N":
    #             suitable_audio_files = audioFiles.filter_by_number(videoFile.number)
    #         image_file_copy = Factory.copyFile(imageFiles.get_list()[0])
    #         image_file_copy.number = videoFile.number
    #         episode = Factory.createEpisode(videoFile, suitable_subs_files, suitable_audio_files, image_file_copy)
    #         episodes_list.add(episode)
    #     return episodes_list


    # @staticmethod
    # def createFilesList(directoryPath=None, configuration=None):
    #     def getSourcePath(directoryPath, configuration):
    #         folders = []
    #         for folderList in classFileOperations.FileOperations.walk(directoryPath):
    #             folders = folderList[1]
    #             break
    #         sourcePath = directoryPath
    #         for folder in folders:
    #             if configuration.isIncludes("sourcePossibleLocation", folder):
    #                 sourcePath = classFileOperations.FileOperations.join(directoryPath, folder)
    #                 if configuration.getValue("linkAudio")[0] == "A":
    #                     configuration.setValue("linkAudio", "N")
    #                 if configuration.getValue("linkSubs")[0] == "A":
    #                     configuration.setValue("linkSubs", "N")
    #                 break
    #         return sourcePath
    #
    #     filesList = classFilesList.FilesList()
    #     if directoryPath is None:
    #         return filesList
    #
    #     langPath = classFileOperations.FileOperations.join(directoryPath, configuration.getValue("langPath")[0])
    #     sourcePath = getSourcePath(directoryPath, configuration)
    #
    #     for file in classFileOperations.FileOperations.listdir(sourcePath):
    #         if classFileOperations.FileOperations.isfile(classFileOperations.FileOperations.join(sourcePath, file)):
    #             filesList.add(Factory.createFile(file, sourcePath, configuration))
    #
    #     for vector in classFileOperations.FileOperations.walk(langPath):
    #         for file in vector[2]:
    #             filesList.add(Factory.createFile(file, vector[0], configuration))
    #     return filesList
