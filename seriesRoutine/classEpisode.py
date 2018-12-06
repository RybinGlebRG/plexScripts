from seriesRoutine import classFile, classFactory


class Episode:

    def __init__(self, episode_number):
        self.video_file = classFactory.Factory.createFilesList()
        self.episode_number = episode_number
        self.image_file = classFactory.Factory.createFilesList()
        self.audio_files = classFactory.Factory.createFilesList()
        self.subs_files = classFactory.Factory.createFilesList()

    def __eq__(self, other):
        if self.episode_number != other.episode_number:
            return False
        if self.video_file != other.video_file:
            return False
        if self.audio_files != other.audio_files:
            return False
        if self.subs_files != other.subs_files:
            return False
        if self.image_file != other.image_file:
            return False

        return True

    def __ne__(self, other):
        if self.episode_number != other.episode_number:
            return True
        if self.video_file != other.video_file:
            return True
        if self.audio_files != other.audio_files:
            return True
        if self.subs_files != other.subs_files:
            return True
        if self.image_file != other.image_file:
            return True

        return False

    def add_video_file(self, video_file):
        self.video_file = video_file

    def add_audio_file(self, audio_file):
        self.audio_files.add(audio_file)

    def add_subs_file(self, subs_file):
        self.subs_files.add(subs_file)

    def add_image_file(self, image_file):
        self.image_file = image_file
