class Searcher:


    def __init__(self, configuration):
        self.configuration = configuration

    def isVideoFile(self, fileName):
        lastDot = fileName.rfind(".")
        suffix = fileName[lastDot + 1:]
        # if suffix in self.configuration.videoFileSuffixes:
        #     return True
        # else:
        #     return False
        # if suffix in self.configuration.getValue("videoFileSuffixes"):
        #     return True
        # else:
        #     return False
        if self.configuration.isIncludes("videoFileSuffixes",suffix):
            return True
        else:
            return False

    def isAudioFile(self, fileName):
        lastDot = fileName.rfind(".")
        suffix = fileName[lastDot + 1:]
        # if suffix in self.configuration.audioFileSuffixes:
        #     return True
        # else:
        #     return False
        # if suffix in self.configuration.getValue("audioFileSuffixes"):
        #     return True
        # else:
        #     return False
        if self.configuration.isIncludes("audioFileSuffixes",suffix):
            return True
        else:
            return False

    def isSubsFile(self, fileName):
        lastDot = fileName.rfind(".")
        suffix = fileName[lastDot + 1:]
        # if suffix in self.configuration.subsFileSuffixes:
        #     return True
        # else:
        #     return False
        # if suffix in self.configuration.getValue("subsFileSuffixes"):
        #     return True
        # else:
        #     return False
        if self.configuration.isIncludes("subsFileSuffixes",suffix):
            return True
        else:
            return False

    def isImageFile(self, fileName):
        lastDot = fileName.rfind(".")
        suffix = fileName[lastDot + 1:]
        if self.configuration.isIncludes("imageFileSuffixes",suffix):
            return True
        else:
            return False
