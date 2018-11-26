from seriesRoutine import classFile, classEpisode


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
                        file.number = configuration.getValueAsList("addFileNumber")[i]

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
            episodesList.append(
                Factory.createEpisode(videoFile, suitableSubsFiles, suitableAudioFiles, Factory.copyFile(imageFile)))
        return episodesList
