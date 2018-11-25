from seriesRoutine import classEpisode
#from seriesRoutine import classImageFile
from seriesRoutine import classFile


class Assemble:

    def __init__(self, configuration):
        self.videoFiles = None
        self.audioFiles = None
        self.subsFiles = None
        self.imageFile=None
        self.configuration = configuration
        self.episodesList = []

    def assemble(self, videoFiles, audioFiles, subsFiles, imageFile):
        self.videoFiles = videoFiles
        self.audioFiles = audioFiles
        self.subsFiles = subsFiles
        self.imageFile=imageFile
        for item in self.videoFiles:
            self.episodesList.append(classEpisode.Episode(item.number))
            self.episodesList[-1].addVideoFile(item)
            # self.episodesList[-1].addImageFile(classImageFile.ImageFile(self.imageFile.fileName,self.imageFile.path))
            # for i in self.episodesList:
            #     print(i.episodeNumber)
            self.episodesList[-1].addImageFile(classFile.File(self.imageFile.fileName, self.imageFile.path))
            if self.configuration.getValue("linkSubs") != "N":
                for file in self.subsFiles:
                    if file.number == self.episodesList[-1].episodeNumber:
                        self.episodesList[-1].addSubsFile(file)
            if self.configuration.getValue("linkAudio") != "N":
                for file in self.audioFiles:
                    if file.number == self.episodesList[-1].episodeNumber:
                        self.episodesList[-1].addAudioFile(file)
