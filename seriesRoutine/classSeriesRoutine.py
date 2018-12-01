import os
from seriesRoutine import classSeriesAnalyzer, classConfiguration, classLink, \
    classPlex
import classLogger
import classFileOperations
import traceback
import sys
from seriesRoutine import classFilesList, classFactory


class SeriesRoutine:

    def __init__(self):
        self.configuration = None
        self.logger = classLogger.Logger()
        self.directoryPath = ""

    # def loadUserConfigurationFile(self, userConfigurationFileName):
    #     self.configuration.load(userConfigurationFileName)
    #     self.configuration.deleteForbiddenSymbolsFromValue("titleName")
    #     self.configuration.formatSeasonNumber()

    # def renameUserConfigurationFile(self, directoryPath, userConfigurationFileName):
    #     classFileOperations.FileOperations.rename(
    #         classFileOperations.FileOperations.join(directoryPath, userConfigurationFileName),
    #         classFileOperations.FileOperations.join(directoryPath,
    #                                                 self.configuration.getValue("configurationFileNameUsed")))

    # def getSourcePath(self, directoryPath):
    #     folders = []
    #     for folderList in classFileOperations.FileOperations.walk(directoryPath):
    #         folders = folderList[1]
    #         break
    #     sourcePath = directoryPath
    #     for folder in folders:
    #         if self.configuration.isIncludes("sourcePossibleLocation", folder):
    #             sourcePath = classFileOperations.FileOperations.join(directoryPath, folder)
    #             if self.configuration.getValue("linkAudio") == "A":
    #                 self.configuration.setValue("linkAudio", "N")
    #             if self.configuration.getValue("linkSubs") == "A":
    #                 self.configuration.setValue("linkSubs", "N")
    #             break
    #     return sourcePath

    # def readFiles(self, directoryPath, sourcePath):
    #     langPath = classFileOperations.FileOperations.join(directoryPath, self.configuration.getValue("langPath"))
    #     filesList = classFilesList.FilesList(self.configuration)
    #
    #     for file in classFileOperations.FileOperations.listdir(sourcePath):
    #         if classFileOperations.FileOperations.isfile(classFileOperations.FileOperations.join(sourcePath, file)):
    #             filesList.append(classFactory.Factory.createFile(file, sourcePath, self.configuration))
    #
    #     for vector in classFileOperations.FileOperations.walk(langPath):
    #         for file in vector[2]:
    #             filesList.append(classFactory.Factory.createFile(file, vector[0], self.configuration))
    #
    #     videoFiles = filesList.filterVideoFiles()
    #     audioFiles = filesList.filterAudioFiles()
    #     subsFiles = filesList.filterSubsFiles()
    #     imageFiles = filesList.filterImageFiles()
    #
    #     return videoFiles, subsFiles, audioFiles, imageFiles[0]

    def logAssemble(self, directory, episodesList):
        episodesList.sort(key=lambda item: item.episodeNumber)
        self.logger.writeLog(directory, "info", "Файлы, сгруппированные по сериям:", "w+")
        for episode in episodesList:
            self.logger.writeLog(directory, "info", "------------------------------------")
            self.logger.writeLog(directory, "info", episode.episodeNumber + ":")
            self.logger.writeLog(directory, "info", episode.videoFile.fileName)
            for audioFile in episode.audioFiles:
                self.logger.writeLog(directory, "info", audioFile.fileName)
            for subsFile in episode.subsFiles:
                self.logger.writeLog(directory, "info", subsFile.fileName)

    def logConfigurationMain(self):
        logger = classLogger.Logger()
        directory = classFileOperations.FileOperations.dirname(classFileOperations.FileOperations.abspath(__file__))
        logger.writeLog(directory, "debug", "configurationMain:", "w+")
        items = self.configuration.getAllPairs()
        for item in items:
            logger.writeLog(directory, "debug", item.key + "=" + item.value)
        logger.writeLog(directory, "debug", "-----------------------------------")

    def refreshPlex(self):
        plex = classPlex.Plex(self.configuration)
        plex.refershLibrary(self.configuration.getValue("plexLibrary"))

    def run(self):
        # self.configuration = classConfiguration.Configuration()
        # self.configuration.load(sys.argv[1])

        # directoryPath, userConfugirationFile = classConfiguration.Configuration.findUserConfigurationFile(
        #     self.configuration.getValue("watcherPath"), self.configuration.getValue("configurationFileName"))
        # if userConfugirationFile == "":
        #     return 1

        try:
            # self.loadUserConfigurationFile(
            #     classFileOperations.FileOperations.join(directoryPath, userConfugirationFile))
            # if not self.configuration.getValue("isTesting"):
            #     self.renameUserConfigurationFile(directoryPath, userConfugirationFile)
            self.configuration = classFactory.Factory.createConfiguration(sys.argv[1])
            if self.configuration is None:
                return None
            directoryPath = self.configuration.getValue("directoryPath")
            #sourcePath = self.getSourcePath(directoryPath)

            filesList = classFactory.Factory.createFilesList(directoryPath, self.configuration)

            videoFiles = filesList.filterVideoFiles()
            audioFiles = filesList.filterAudioFiles()
            subsFiles = filesList.filterSubsFiles()
            imageFile = filesList.filterImageFiles()[0]

            # videoFiles, subsFiles, audioFiles, imageFile = self.readFiles(directoryPath, sourcePath)

            classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(videoFiles)
            classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(subsFiles)
            classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(audioFiles)

            episodesList = classFactory.Factory.createEpisodesList(videoFiles, subsFiles, audioFiles, imageFile,
                                                                   self.configuration)

            self.logAssemble(directoryPath, episodesList)

            link = classLink.Link(self.configuration)
            link.prepareFiles(episodesList)
            link.checkTarget()
            link.createLinks(episodesList)

            isSuccessfull = False
            cnt = 0
            while not isSuccessfull:
                try:
                    self.refreshPlex()
                    isSuccessfull = True
                except Exception as e:
                    cnt += 1
                    if cnt == 10:
                        raise Exception(str(e))


        except Exception as e:
            logger = classLogger.Logger()
            logger.writeLog(self.configuration.getValue("directoryPath"), "error", str(e))
            traceback.print_exc()

        # TODO: Добавление файлов поодиночке
        # TODO: Файлы, имя которых отличается не только номером серии
        # TODO: Watcher должен работать с несколькими файлами, а не только одним
