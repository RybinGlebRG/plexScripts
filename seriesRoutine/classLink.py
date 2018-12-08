import classFileOperations


class Link:

    def __init__(self, configuration):
        self.configuration = configuration

    def prepareFiles(self, episodesList):
        def incrementCounter(cnt):
            if cnt == "":
                cnt = ".2"
            else:
                cnt = cnt.lstrip(".")
                cnt = int(cnt) + 1
                cnt = str(cnt)
                cnt = "." + cnt
            return cnt

        max_num = 0
        for item in episodesList:
            if item.episode_number > max_num:
                max_num = item.episodeNumber
        max_num = len(str(max_num))

        seasonNumber = self.configuration.getValue("seasonNumber")

        titleName = self.configuration.getValue("titleName")
        for episode in episodesList:
            episode.video_file.linkFileName = titleName + " - s" + seasonNumber + "e" + (
                str(episode.episode_number)).zfill(max_num) + \
                                             "." + episode.video_file.getSuffix()
            episode.imageFile.linkFileName = titleName + " - s" + seasonNumber + "e" + (
                str(episode.episode_number)).zfill(max_num) + \
                                             "." + episode.imageFile.getSuffix()
            # print(episode.videoFile.linkFileName)
            # print(episode.imageFile.linkFileName)
            counter = ""
            for item in episode.audioFiles:
                item.linkFileName = titleName + " - s" + seasonNumber + "e" + (str(
                    episode.episode_number)).zfill(max_num) + counter + "." + item.getSuffix()
                counter = incrementCounter(counter)
            counter = ""
            for item in episode.subsFiles:
                # print(counter)
                item.linkFileName = titleName + " - s" + seasonNumber + "e" + (str(
                    episode.episode_number)).zfill(max_num) + counter + "." + item.getSuffix()
                counter = incrementCounter(counter)

    def checkTarget(self):
        targetPath = self.configuration.getValue("targetPath")
        titleName = self.configuration.getValue("titleName")
        seasonNumber = self.configuration.getValue("seasonNumber")
        titleExists = classFileOperations.FileOperations.exists(
            classFileOperations.FileOperations.join(targetPath, titleName))
        seasonExists = False
        if titleExists:
            seasonExists = classFileOperations.FileOperations.exists(
                classFileOperations.FileOperations.join(classFileOperations.FileOperations.join(targetPath, titleName),
                                                        "Season " + seasonNumber))
            if seasonExists:
                classFileOperations.FileOperations.rmtree(
                    classFileOperations.FileOperations.join(
                        classFileOperations.FileOperations.join(targetPath, titleName), "Season " + seasonNumber))
                classFileOperations.FileOperations.makedirs(
                    classFileOperations.FileOperations.join(
                        classFileOperations.FileOperations.join(targetPath, titleName), "Season " + seasonNumber))
            else:
                classFileOperations.FileOperations.makedirs(
                    classFileOperations.FileOperations.join(
                        classFileOperations.FileOperations.join(targetPath, titleName),
                        "Season " + seasonNumber))
        else:
            classFileOperations.FileOperations.makedirs(classFileOperations.FileOperations.join(targetPath, titleName))
            classFileOperations.FileOperations.makedirs(
                classFileOperations.FileOperations.join(classFileOperations.FileOperations.join(targetPath, titleName),
                                                        "Season " + seasonNumber))

    def createLinks(self, episodesList):
        if not self.configuration.isIncludes("wrongOSNames", classFileOperations.FileOperations.osName()):
            # print("LOL")
            targetPath = self.configuration.getValue("targetPath")
            titleName = self.configuration.getValue("titleName")
            seasonNumber = self.configuration.getValue("seasonNumber")
            targetFolder = classFileOperations.FileOperations.join(
                classFileOperations.FileOperations.join(targetPath, titleName), "Season " + seasonNumber)
            mountPoint = self.configuration.getValue("mountPoint")
            trueMountPoint = self.configuration.getValue("trueMountPoint")
            for episode in episodesList:
                classFileOperations.FileOperations.symlink(classFileOperations.FileOperations.join(
                    episode.video_file.path.replace(mountPoint, trueMountPoint),
                    episode.video_file.fileName)
                    , classFileOperations.FileOperations.join(targetFolder, episode.video_file.linkFileName))
                classFileOperations.FileOperations.symlink(classFileOperations.FileOperations.join(
                    episode.imageFile.path.replace(mountPoint, trueMountPoint),
                    episode.imageFile.fileName)
                    , classFileOperations.FileOperations.join(targetFolder, episode.imageFile.linkFileName))
                for item in episode.subsFiles:
                    classFileOperations.FileOperations.symlink(classFileOperations.FileOperations.join(
                        item.path.replace(mountPoint, trueMountPoint),
                        item.fileName)
                        , classFileOperations.FileOperations.join(targetFolder, item.linkFileName))
                for item in episode.audioFiles:
                    classFileOperations.FileOperations.symlink(classFileOperations.FileOperations.join(
                        item.path.replace(mountPoint, trueMountPoint),
                        item.fileName)
                        , classFileOperations.FileOperations.join(targetFolder, item.linkFileName))
