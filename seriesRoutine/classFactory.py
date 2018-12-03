from seriesRoutine import classFile, classEpisode, classConfiguration, classFilesList
import classFileOperations


class Factory:

    def __init__(self, configuration):
        pass
        # self.configuration = configuration

    @staticmethod
    def checkIfSpecified(file, configuration):
        if configuration is not None:
            if configuration.isIncludes("addFile", file.fileName):
                addFiles = configuration.getValueAsList("addFile")
                for i in range(0, len(addFiles)):
                    if addFiles[i] == file.fileName:
                        file.number = configuration.getValueAsList("addFileNumber")[i].lstrip("")
                        if file.number == "":
                            file.number = 0
                        else:
                            file.number = int(file.number)

    @staticmethod
    def createFile(fileName, path, configuration=None):
        file = classFile.File(fileName, path)
        Factory.checkIfSpecified(file, configuration)
        return file

    @staticmethod
    def copyFile(file):
        newFile = Factory.createFile(file.fileName, file.path)
        newFile.number = file.number
        newFile.possibleSeriesNumbers = file.possibleSeriesNumbers
        newFile.linkFileName = file.linkFileName
        return newFile

    @staticmethod
    def createEpisode(videoFile, subsFiles, audioFiles, imageFile):
        episode = classEpisode.Episode(videoFile.number)
        episode.addVideoFile(videoFile)
        for subsFile in subsFiles:
            episode.addSubsFile(subsFile)
        for audioFile in audioFiles:
            episode.addAudioFile(audioFile)
        episode.addImageFile(imageFile)
        return episode

    @staticmethod
    def createEpisodesList(videoFiles, subsFiles, audioFiles, imageFile, configuration):
        episodesList = []
        for videoFile in videoFiles:
            suitableSubsFiles = []
            if configuration.getValue("linkSubs") != "N":
                for subsFile in subsFiles:
                    if subsFile.number == videoFile.number:
                        suitableSubsFiles.append(subsFile)
            suitableAudioFiles = []
            if configuration.getValue("linkAudio") != "N":
                for audioFile in audioFiles:
                    if audioFile.number == videoFile.number:
                        suitableAudioFiles.append(audioFile)
            image_file_copy = Factory.copyFile(imageFile)
            image_file_copy.number = videoFile.number
            episodesList.append(
                Factory.createEpisode(videoFile, suitableSubsFiles, suitableAudioFiles, image_file_copy))
        return episodesList

    @staticmethod
    def createConfiguration(absoluteFileName):
        configuration = classConfiguration.Configuration()
        configuration.load(absoluteFileName)
        configuration.checkWatcherPath()
        # print(configuration.getValue("watcherPath"))
        directoryPath, userConfugirationFile = classConfiguration.Configuration.findUserConfigurationFile(
            configuration.getValue("watcherPath"), configuration.getValue("configurationFileName"))
        if userConfugirationFile == "":
            return None
        configuration.createKey("directoryPath", directoryPath)
        configuration.load(classFileOperations.FileOperations.join(directoryPath, userConfugirationFile))
        configuration.deleteForbiddenSymbolsFromValue("titleName")
        configuration.formatSeasonNumber()

        classFileOperations.FileOperations.rename(
            classFileOperations.FileOperations.join(directoryPath,
                                                    classFileOperations.FileOperations.join(directoryPath,
                                                                                            userConfugirationFile)),
            classFileOperations.FileOperations.join(directoryPath,
                                                    configuration.getValue("configurationFileNameUsed")))
        return configuration

    @staticmethod
    def createFilesList(directoryPath, configuration, list=None):
        def getSourcePath(directoryPath, configuration):
            folders = []
            for folderList in classFileOperations.FileOperations.walk(directoryPath):
                folders = folderList[1]
                break
            sourcePath = directoryPath
            for folder in folders:
                if configuration.isIncludes("sourcePossibleLocation", folder):
                    sourcePath = classFileOperations.FileOperations.join(directoryPath, folder)
                    if configuration.getValue("linkAudio") == "A":
                        configuration.setValue("linkAudio", "N")
                    if configuration.getValue("linkSubs") == "A":
                        configuration.setValue("linkSubs", "N")
                    break
            return sourcePath

        langPath = classFileOperations.FileOperations.join(directoryPath, configuration.getValue("langPath"))
        filesList = classFilesList.FilesList(configuration)
        sourcePath = getSourcePath(directoryPath, configuration)

        for file in classFileOperations.FileOperations.listdir(sourcePath):
            if classFileOperations.FileOperations.isfile(classFileOperations.FileOperations.join(sourcePath, file)):
                filesList.add(Factory.createFile(file, sourcePath, configuration))

        for vector in classFileOperations.FileOperations.walk(langPath):
            for file in vector[2]:
                filesList.add(Factory.createFile(file, vector[0], configuration))
        return filesList
