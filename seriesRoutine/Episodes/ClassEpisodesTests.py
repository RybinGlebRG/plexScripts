from seriesRoutine.Episodes import ClassEpisodesList
from seriesRoutine import classFilesList, classFile


class EpisodesTests:

    def __init__(self):
        self.cases = []

    def case_1(self):
        """
        This case tests ability to form episodes from files.
        Files does not have any kind of special organization.
        """

        def arrange():
            video_files = classFilesList.FilesList()
            subs_files = classFilesList.FilesList()
            audio_files = classFilesList.FilesList()
            image_files = classFilesList.FilesList()

            video_files.add(classFile.File("1.mkv",'/'))
            video_files.add(classFile.File("2.mkv", '/'))
            video_files.add(classFile.File("3.mkv", '/'))

            # TODO: Add other test files
            return video_files, subs_files, audio_files, image_files

        def act(video_files, subs_files, audio_files, image_files):
            episodes_list = ClassEpisodesList.EpisodesList()
            episodes_list.load(video_files, subs_files, audio_files, image_files)
            return episodes_list

        def check(episides_list):
            pass

        video_files, subs_files, audio_files, image_files = arrange()
        episodes_list = act(video_files, subs_files, audio_files, image_files)

        return check(episodes_list)

    def run(self):
        self.cases.append(self.case_1)

        for case in self.cases:
            if not case():
                return False
        return True
