from seriesRoutine import classFactory, classSeriesAnalyzer, classKeyValue, classEpisode
from tests.testData.case_1 import check, prepare
import sys
import classFileOperations


def get_model_list():
    episodes_list = []
    for i in [1, 2, 10]:
        episode = classEpisode.Episode(i)
        path = classFileOperations.FileOperations.abspath(__file__)
        path = classFileOperations.FileOperations.dirname(path)
        path = classFileOperations.FileOperations.join(path, "Some serial")
        video_file = classFactory.Factory.createFile("some episode" + str(i) + ".mkv", path)
        video_file.possibleSeriesNumbers = [i]
        video_file.number = i
        episode.addVideoFile(video_file)

        image_file = classFactory.Factory.createFile("some.jpg", path)
        image_file.number = i

        path = classFileOperations.FileOperations.join(path, "Lang")
        audio_path = classFileOperations.FileOperations.join(path, "Sound")
        audio_file = classFactory.Factory.createFile(str(i) + ".ac3", audio_path)
        audio_file.possibleSeriesNumbers = [i, 3]
        audio_file.number = i

        subs_path = classFileOperations.FileOperations.join(path, "Subs")
        subs_file = classFactory.Factory.createFile("some episode" + str(i) + ".ass", subs_path)
        subs_file.possibleSeriesNumbers = [i]
        subs_file.number = i

        episode.addAudioFile(audio_file)
        episode.addSubsFile(subs_file)
        episode.addImageFile(image_file)
        episodes_list.append(episode)

    return episodes_list


def prepare_conf():
    prepare.prepare()