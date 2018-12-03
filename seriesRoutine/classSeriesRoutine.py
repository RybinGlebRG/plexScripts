import os
from seriesRoutine import classSeriesAnalyzer, classConfiguration, classLink, \
    classPlex, ClassEpisodesList
import classLogger
import classFileOperations
import traceback
import sys
from seriesRoutine import classFilesList, classFactory


class SeriesRoutine:

    def __init__(self):
        pass
        #self.configuration = None
        # self.log_path=None
        # self.logger = classLogger.Logger()
        # self.directoryPath = ""

    # def logAssemble(self, directory, episodesList):
    #     episodesList.sort(key=lambda item: item.episodeNumber)
    #     self.logger.writeLog(directory, "info", "Файлы, сгруппированные по сериям:", "w+")
    #     for episode in episodesList:
    #         self.logger.writeLog(directory, "info", "------------------------------------")
    #         self.logger.writeLog(directory, "info", str(episode.episodeNumber) + ":")
    #         self.logger.writeLog(directory, "info", episode.videoFile.fileName)
    #         for audioFile in episode.audioFiles:
    #             self.logger.writeLog(directory, "info", audioFile.fileName)
    #         for subsFile in episode.subsFiles:
    #             self.logger.writeLog(directory, "info", subsFile.fileName)

    # def logConfigurationMain(self):
    #     logger = classLogger.Logger()
    #     directory = classFileOperations.FileOperations.dirname(classFileOperations.FileOperations.abspath(__file__))
    #     logger.writeLog(directory, "debug", "configurationMain:", "w+")
    #     items = self.configuration.getAllPairs()
    #     for item in items:
    #         logger.writeLog(directory, "debug", item.key + "=" + item.value)
    #     logger.writeLog(directory, "debug", "-----------------------------------")

    def refreshPlex(self,configuration):
        plex = classPlex.Plex(configuration)
        plex.refershLibrary(configuration.getValue("plexLibrary"))

    def run(self):
        log_path = None
        try:
            configuration = classFactory.Factory.createConfiguration(sys.argv[1])
            if configuration is None:
                return None
            directoryPath = configuration.getValue("directoryPath")
            log_path = directoryPath
            filesList = classFactory.Factory.createFilesList(directoryPath, configuration)

            videoFiles = filesList.filterVideoFiles()
            audioFiles = filesList.filterAudioFiles()
            subsFiles = filesList.filterSubsFiles()
            imageFiles = filesList.filterImageFiles()

            classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(videoFiles.get_list())
            classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(subsFiles.get_list())
            classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(audioFiles.get_list())

            episodes_list = classFactory.Factory.createEpisodesList(videoFiles.get_list(), subsFiles.get_list(),
                                                                    audioFiles.get_list(), imageFiles.get_list()[0],
                                                                    configuration)

            episodes_list.log(directoryPath)

            # self.logAssemble(directoryPath, episodesList)

            link = classLink.Link(configuration)
            link.prepareFiles(episodes_list.episodes_list)
            link.checkTarget()
            link.createLinks(episodes_list.episodes_list)

            isSuccessfull = False
            cnt = 0
            while not isSuccessfull:
                try:
                    self.refreshPlex(configuration)
                    isSuccessfull = True
                except Exception as e:
                    cnt += 1
                    if cnt == 10:
                        raise Exception(str(e))


        except Exception as e:
            logger = classLogger.Logger()
            if log_path is None:
                path = classFileOperations.FileOperations.abspath(__file__)
                path = classFileOperations.FileOperations.dirname(path)
            else:
                path = log_path
            logger.writeLog(path, "error", str(e))
            traceback.print_exc()

        # TODO: Добавление файлов поодиночке
        # TODO: Файлы, имя которых отличается не только номером серии
        # TODO: Watcher должен работать с несколькими файлами, а не только одним
        # TODO: Номер серии должен быть представлен числом. В том числе, когда указан в пользовательской конфигурации

        print("END")
