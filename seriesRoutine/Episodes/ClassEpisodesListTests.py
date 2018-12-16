from seriesRoutine.Episodes import ClassEpisodesList
from seriesRoutine.Files import classFile, classFilesList


class EpisodesTests:

    def __init__(self):
        self.cases = []

    def case_1(self):
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

            return l_video_files, l_subs_files, l_audio_files, l_image_files

        def act(p_video_files, p_subs_files, p_audio_files, p_image_files):
            l_episodes_list = ClassEpisodesList.EpisodesList()
            l_episodes_list.load(p_video_files, p_subs_files, p_audio_files, p_image_files)
            return l_episodes_list

        def check(p_episodes_list):
            for episode in p_episodes_list:
                n = episode.episode_number
                if episode.video_file.number != n:
                    return False
                if episode.video_file.fileName != str(n) + ".mkv":
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
                if episode.image_file.number != n:
                    return False
            return True

        video_files, subs_files, audio_files, image_files = arrange()
        episodes_list = act(video_files, subs_files, audio_files, image_files)
        result = check(episodes_list)

        return result

    def case_2(self):
        """
        This case tests ability to form episodes from two groups of video files - "Bleach case"
        """
        raise NotImplementedError

    def run(self):
        self.cases.append(self.case_1)
        self.cases.append(self.case_2)

        for case in self.cases:
            if not case():
                return False
        return True
