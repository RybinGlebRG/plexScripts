from seriesRoutine.Episodes import ClassEpisodesList
from seriesRoutine.Files import classFile, classFilesList
from common import TestCase


def general_case():
    """
    This case tests general ability to form episodes from files.
    Files already have numbers assigned.
    Files does not have any kind of special organization.
    """

    def arrange():
        l_video_files = classFilesList.FilesList()
        l_subs_files = classFilesList.FilesList()
        l_audio_files = classFilesList.FilesList()
        l_image_files = classFilesList.FilesList()

        l_video_files.add(classFile.File("1.mkv", '/', 1))
        l_video_files.add(classFile.File("2.mkv", '/', 2))
        l_video_files.add(classFile.File("3.mkv", '/', 3))

        l_audio_files.add(classFile.File("1.ac3", "/Lang/Audio/1", 1))
        l_audio_files.add(classFile.File("2.ac3", "/Lang/Audio/1", 2))
        l_audio_files.add(classFile.File("3.ac3", "/Lang/Audio/1", 3))

        l_audio_files.add(classFile.File("1.ac3", "/Lang/Audio/2", 1))
        l_audio_files.add(classFile.File("2.ac3", "/Lang/Audio/2", 2))
        l_audio_files.add(classFile.File("3.ac3", "/Lang/Audio/2", 3))

        l_subs_files.add(classFile.File("1.ass", "/Lang/Subs/1", 1))
        l_subs_files.add(classFile.File("2.ass", "/Lang/Subs/1", 2))
        l_subs_files.add(classFile.File("3.ass", "/Lang/Subs/1", 3))

        l_subs_files.add(classFile.File("1.ass", "/Lang/Subs/2", 1))
        l_subs_files.add(classFile.File("2.ass", "/Lang/Subs/2", 2))
        l_subs_files.add(classFile.File("3.ass", "/Lang/Subs/2", 3))

        l_image_files.add(classFile.File("image.jpg", "/"))

        return [l_video_files, l_subs_files, l_audio_files, l_image_files]

    def act(p_input):
        p_video_files = p_input[0]
        p_subs_files = p_input[1]
        p_audio_files = p_input[2]
        p_image_files = p_input[3]
        l_episodes_list = ClassEpisodesList.EpisodesList()
        l_episodes_list.load(p_video_files, p_subs_files, p_audio_files, p_image_files)
        return [l_episodes_list]

    def check(p_input):
        p_episodes_list = p_input[0]
        for episode in p_episodes_list:
            n = episode.episode_number
            for video_file in episode.video_files:
                if video_file.number != n:
                    return False
                if video_file.fileName != str(n) + ".mkv":
                    return False
            for audio_file in episode.audio_files:
                if audio_file.number != n:
                    return False
                if audio_file.fileName != str(n) + ".ac3":
                    return False
            for subs_file in episode.subs_files:
                if subs_file.number != n:
                    return False
                if subs_file.fileName != str(n) + ".ass":
                    return False
            for image_file in episode.image_files:
                if image_file.number != n:
                    return False
        return True

    test_case = TestCase.TestCase(arrange, act, check)
    test_case.description = "EpisodesList General Case"
    return test_case
