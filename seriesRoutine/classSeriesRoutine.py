from seriesRoutine import classLink, \
    classPlex
from seriesRoutine.Episodes import ClassEpisodesList
from seriesRoutine.Configuration import classConfiguration
from seriesRoutine.Analyzer import classSeriesAnalyzer
import classLogger
import classFileOperations
import traceback
import sys
from seriesRoutine import classFilesList


class SeriesRoutine:

    def __init__(self):
        pass

    def refreshPlex(self, configuration):
        plex = classPlex.Plex(configuration)
        plex.refershLibrary(configuration.getValue("plexLibrary")[0])

    def run(self):
        log_path = None
        try:
            configuration = classConfiguration.Configuration()
            configuration.load(sys.argv[1])
            if not configuration.is_ready():
                return None
            directory_path = configuration.getValue("directoryPath")[0]

            log_path = directory_path
            filesList = classFilesList.FilesList()
            filesList.load(directory_path, configuration)

            video_files = filesList.filter_by_suffixes(configuration.getValue("videoFileSuffixes"))
            audio_files = filesList.filter_by_suffixes(configuration.getValue("audioFileSuffixes"))
            subs_files = filesList.filter_by_suffixes(configuration.getValue("subsFileSuffixes"))
            image_files = filesList.filter_by_suffixes(configuration.getValue("imageFileSuffixes"))

            classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(video_files)
            classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(subs_files)
            classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(audio_files)

            episodes_list = ClassEpisodesList.EpisodesList()
            episodes_list.load(video_files, subs_files, audio_files, image_files)

            episodes_list.log(directory_path)

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
