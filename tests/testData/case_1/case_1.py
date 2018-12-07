from seriesRoutine import classFactory, classEpisode, ClassEpisodesList
from seriesRoutine.Analyzer import classSeriesAnalyzer
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
    episodes_list = []
    for i in range(1, 4):
        episode = classEpisode.Episode(i)
        path = classFileOperations.FileOperations.abspath(__file__)
        path = classFileOperations.FileOperations.dirname(path)
        path = classFileOperations.FileOperations.join(path, "Some serial")
        video_file = classFactory.Factory.createFile("some episode" + str(i) + ".mkv", path)
        video_file.possibleSeriesNumbers = [i]
        video_file.number = i
        episode.add_video_file(video_file)

        image_file = classFactory.Factory.createFile("some.jpg", path)
        image_file.number = i

        path = classFileOperations.FileOperations.join(path, "Lang")
        audio_path = classFileOperations.FileOperations.join(path, "Sound")
        audio_file = classFactory.Factory.createFile("some episode" + str(i) + ".ac3", audio_path)
        audio_file.possibleSeriesNumbers = [i, 3]
        audio_file.number = i

        subs_path = classFileOperations.FileOperations.join(path, "Subs")
        subs_file = classFactory.Factory.createFile("some episode" + str(i) + ".ass", subs_path)
        subs_file.possibleSeriesNumbers = [i]
        subs_file.number = i

        episode.add_audio_file(audio_file)
        episode.add_subs_file(subs_file)
        episode.add_image_file(image_file)
        episodes_list.append(episode)
        episodes_list_new = ClassEpisodesList.EpisodesList()
        episodes_list_new.episodes_list = episodes_list
    return episodes_list_new


def prepare_conf():
    prepare.prepare()
