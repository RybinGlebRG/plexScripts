class Episode:

    def __init__(self,episodeNumber):
        self.videoFile=None
        self.audioFiles=[]
        self.subsFiles=[]
        self.episodeNumber=episodeNumber
        self.imageFile=None

    def addVideoFile(self,videoFile):
        self.videoFile=videoFile

    def addAudioFile(self,audioFile):
        self.audioFiles.append(audioFile)

    def addSubsFile(self,subsFile):
        self.subsFiles.append(subsFile)

    def addImageFile(self,imageFile):
        self.imageFile=imageFile
