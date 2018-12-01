from seriesRoutine import classFactory, classSeriesAnalyzer
from tests.testData.case_1 import check, prepare
import sys


def run():
    prepare.prepare()

    configuration = classFactory.Factory.createConfiguration(sys.argv[1])
    directoryPath = configuration.getValue("directoryPath")
    filesList = classFactory.Factory.createFilesList(directoryPath, configuration)

    videoFiles = filesList.filterVideoFiles()
    audioFiles = filesList.filterAudioFiles()
    subsFiles = filesList.filterSubsFiles()
    imageFile = filesList.filterImageFiles()[0]

    classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(videoFiles)
    classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(subsFiles)
    classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(audioFiles)

    episodesList = classFactory.Factory.createEpisodesList(videoFiles, subsFiles, audioFiles, imageFile,
                                                           configuration)
    result = check.check(episodesList)
    return result
