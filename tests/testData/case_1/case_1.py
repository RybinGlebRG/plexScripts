from seriesRoutine import classFactory, classSeriesAnalyzer, classKeyValue
from tests.testData.case_1 import check, prepare
import sys
import classFileOperations


def prepare_test_configuration(configuration):
    configuration.addTestData("videoFileSuffixes", "mkv")
    configuration.addTestData("audioFileSuffixes", "ac3")
    configuration.addTestData("subsFileSuffixes", "ass")
    configuration.addTestData("imageFileSuffixes", "jpg")
    configuration.addTestData("linkAudio", "A")
    configuration.addTestData("linkSubs", "A")
    configuration.addTestData("langPath", "Lang")
    configuration.addTestData("sourcePossibleLocation", "merged")
    configuration.addTestData("directoryPathArgumentNumber", "1")
    path = classFileOperations.FileOperations.abspath(sys.argv[0])
    ldir = classFileOperations.FileOperations.dirname(path)
    configuration.addTestData("watcherPath", ldir)
    configuration.addTestData("configurationFileName", "configuration.ready")
    configuration.addTestData("configurationFileNameUsed", "configuration.txt")
    configuration.addTestData("forbiddenSymbols", list('\/*?"<>|'))
    configuration.addTestData("wrongOSNames", "nt")
    configuration.addTestData("seasonNumber", "01")
    configuration.addTestData("titleName", "Some")
    path = classFileOperations.FileOperations.abspath(sys.argv[0])
    path = classFileOperations.FileOperations.dirname(path)
    path = classFileOperations.FileOperations.join(path, "testData")
    path = classFileOperations.FileOperations.join(path, "case_1")
    path = classFileOperations.FileOperations.join(path, "Some serial")
    configuration.addTestData("directoryPath", path)


def prepare_test_video_files(video_files):
    pass


def run():
    prepare.prepare()

    configuration = classFactory.Factory.createConfiguration(sys.argv[1])
    prepare_test_configuration(configuration)
    configuration.test()

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

def get_model_list():
    pass
