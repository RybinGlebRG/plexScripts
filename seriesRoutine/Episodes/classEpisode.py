from seriesRoutine.Files import classFilesList


class Episode:

    def __init__(self, episode_number):
        self.video_files = classFilesList.FilesList()
        self.episode_number = episode_number
        self.image_files = classFilesList.FilesList()
        self.audio_files = classFilesList.FilesList()
        self.subs_files = classFilesList.FilesList()

    def __eq__(self, other):
        if self.episode_number != other.episode_number:
            return False
        if self.video_files != other.video_file:
            return False
        if self.audio_files != other.audio_files:
            return False
        if self.subs_files != other.subs_files:
            return False
        if self.image_files != other.image_file:
            return False

        return True

    def __ne__(self, other):
        if self.episode_number != other.episode_number:
            return True
        if self.video_files != other.video_file:
            return True
        if self.audio_files != other.audio_files:
            return True
        if self.subs_files != other.subs_files:
            return True
        if self.image_files != other.image_file:
            return True

        return False

    def add_video_file(self, video_file):
        self.video_files.add(video_file)

    def add_audio_file(self, audio_file):
        self.audio_files.add(audio_file)

    def add_subs_file(self, subs_file):
        self.subs_files.add(subs_file)

    def add_image_file(self, image_file):
        self.image_files.add(image_file)

    def delete_specified(self, configuration):
        if configuration.getValue("linkSubs")[0] != "N":
            self.subs_files.clear()
        if configuration.getValue("linkAudio")[0] != "N":
            self.audio_files.clear()
