from seriesRoutine import classLink, \
    classPlex
from seriesRoutine.Episodes import ClassEpisodesList
from seriesRoutine.Configuration import classConfiguration
from seriesRoutine.Analyzer import ClassSeriesAnalyzer
import classLogger
import classFileOperations
import traceback
import sys
from seriesRoutine.Files import classFilesList


class SeriesRoutine:

    def __init__(self):
        pass

    # def refreshPlex(self, configuration):
    #     plex = classPlex.Plex(configuration)
    #     plex.refershLibrary(configuration.getValue("plexLibrary")[0])

    def run(self):
        log_path = None
        try:
            logger = classLogger.Logger()
            configuration = classConfiguration.Configuration()
            configuration.load(sys.argv[1])
            if not configuration.is_ready():
                return None
            logger.writeLog(
                classFileOperations.FileOperations.dirname(classFileOperations.FileOperations.abspath(__file__)),
                configuration.log(),
                level="debug",
                mode="w+")
            directory_path = configuration.getValue("directoryPath")[0]

            log_path = directory_path

            video_files = classFilesList.FilesList()
            video_files.load(configuration.getValue("source_path"), configuration.getValue("videoFileSuffixes"),
                             configuration, is_recursive=False)

            audio_files = classFilesList.FilesList()
            audio_files.load(configuration.getValue("lang_path"), configuration.getValue("audioFileSuffixes"),
                             configuration)

            subs_files = classFilesList.FilesList()
            subs_files.load(configuration.getValue("lang_path"), configuration.getValue("subsFileSuffixes"),
                            configuration)

            image_files = classFilesList.FilesList()
            image_files.load(configuration.getValue("source_path"), configuration.getValue("imageFileSuffixes"),
                             configuration, is_recursive=False)

            ClassSeriesAnalyzer.SeriesAnalyzer.setFileNumber(video_files)
            ClassSeriesAnalyzer.SeriesAnalyzer.setFileNumber(subs_files)
            ClassSeriesAnalyzer.SeriesAnalyzer.setFileNumber(audio_files)

            episodes_list = ClassEpisodesList.EpisodesList()
            episodes_list.load(video_files, subs_files, audio_files, image_files)

            episodes_list_log = episodes_list.log()

            logger.writeLog(directory_path, episodes_list_log, mode="w+")

            link = classLink.Link(configuration)
            # link.prepareFiles(episodes_list.episodes_list)
            # link.checkTarget()
            # TODO: Make following function entry point
            link.createLinks(episodes_list.episodes_list)

            plex = classPlex.Plex(configuration)
            plex.refresh_library(configuration.getValue("plexLibrary")[0])

        except Exception as e:
            logger = classLogger.Logger()
            if log_path is None:
                path = classFileOperations.FileOperations.abspath(__file__)
                path = classFileOperations.FileOperations.dirname(path)
            else:
                path = log_path
            logger.writeLog(path, [str(e)], "error")
            traceback.print_exc()

        # TODO: Watcher должен работать с несколькими файлами, а не только одним

        # print("END")
