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
        # self.configuration = None
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

    def refreshPlex(self, configuration):
        plex = classPlex.Plex(configuration)
        plex.refershLibrary(configuration.getValue("plexLibrary")[0])

    def run(self):
        log_path = None
        try:
            configuration = classFactory.Factory.createConfiguration(sys.argv[1])
            if configuration is None:
                return None
            directoryPath = configuration.getValue("directoryPath")[0]
            log_path = directoryPath
            filesList = classFactory.Factory.createFilesList(directoryPath, configuration)

            video_files = filesList.filter_by_suffixes(configuration.getValue("videoFileSuffixes"))
            audio_files = filesList.filter_by_suffixes(configuration.getValue("audioFileSuffixes"))
            subs_files = filesList.filter_by_suffixes(configuration.getValue("subsFileSuffixes"))
            image_files = filesList.filter_by_suffixes(configuration.getValue("imageFileSuffixes"))

            classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(video_files)
            classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(subs_files)
            classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(audio_files)

            episodes_list = classFactory.Factory.createEpisodesList(video_files, subs_files,
                                                                    audio_files, image_files,
                                                                    configuration)

            episodes_list.log(directoryPath)

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

        # TODO: Watcher должен работать с несколькими файлами, а не только одним

        # print("END")
