from seriesRoutine import classFactory
from seriesRoutine.Episodes import classEpisode
from tests.testData.case_1 import prepare
import classFileOperations

def get_model_list():
    episodes_list = []
    for i in range(1, 5):
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

    episode = classEpisode.Episode(5)
    path = classFileOperations.FileOperations.abspath(__file__)
    path = classFileOperations.FileOperations.dirname(path)
    path = classFileOperations.FileOperations.join(path, "Some serial")
    video_file = classFactory.Factory.createFile("some ep five.mkv", path)
    video_file.possibleSeriesNumbers = [5]
    video_file.number = 5
    episode.add_video_file(video_file)

    image_file = classFactory.Factory.createFile("some.jpg", path)
    image_file.number = 5

    path = classFileOperations.FileOperations.join(path, "Lang")
    audio_path = classFileOperations.FileOperations.join(path, "Sound")
    audio_file = classFactory.Factory.createFile("some ep five.ac3", audio_path)
    audio_file.possibleSeriesNumbers = [5, 3]
    audio_file.number = 5

    subs_path = classFileOperations.FileOperations.join(path, "Subs")
    subs_file = classFactory.Factory.createFile("some ep five.ass", subs_path)
    subs_file.possibleSeriesNumbers = [5]
    subs_file.number = 5

    episode.add_audio_file(audio_file)
    episode.add_subs_file(subs_file)
    episode.add_image_file(image_file)
    episodes_list.append(episode)
    return episodes_list


def prepare_conf():
    prepare.prepare()