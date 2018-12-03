from seriesRoutine import classFile


class Episode:

    def __init__(self, episodeNumber):
        self.videoFile = None
        self.audioFiles = []
        self.subsFiles = []
        self.episodeNumber = episodeNumber
        self.imageFile = None

    def addVideoFile(self, videoFile):
        self.videoFile = videoFile

    def addAudioFile(self, audioFile):
        self.audioFiles.append(audioFile)

    def addSubsFile(self, subsFile):
        self.subsFiles.append(subsFile)

    def addImageFile(self, imageFile):
        self.imageFile = imageFile

    @staticmethod
    def are_equal(episode_1, episode_2):
        equal = True
        if not classFile.File.are_equal(episode_1.videoFile, episode_2.videoFile):
            print("1")
            equal = False
        if len(episode_1.audioFiles) != len(episode_2.audioFiles):
            print("2")
            equal = False
        else:
            for i in range(0, len(episode_1.audioFiles)):
                if not classFile.File.are_equal(episode_1.audioFiles[i], episode_2.audioFiles[i]):
                    print("3")
                    equal = False
        if len(episode_1.subsFiles) != len(episode_2.subsFiles):
            print("4")
            equal = False
        else:
            for i in range(0, len(episode_1.subsFiles)):
                if not classFile.File.are_equal(episode_1.subsFiles[i], episode_2.subsFiles[i]):
                    print("5")
                    equal = False
        if episode_1.episodeNumber != episode_2.episodeNumber:
            print("6")
            equal = False
        if not classFile.File.are_equal(episode_1.imageFile, episode_2.imageFile):
            print("7")
            equal = False

        return equal
