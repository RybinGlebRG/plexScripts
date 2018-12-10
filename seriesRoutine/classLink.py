import classFileOperations


class Link:

    def __init__(self, configuration):
        self.configuration = configuration
        self.season_number = self.configuration.getValue("seasonNumber")[0]
        self.title_name = self.configuration.getValue("titleName")[0]
        self.target_path = self.configuration.getValue("targetPath")[0]
        self.mount_point = self.configuration.getValue("mountPoint")[0]
        self.true_mount_point = self.configuration.getValue("trueMountPoint")[0]

    def prepare_files(self, episodes_list, title_name, season_number):
        def increment_counter(cnt):
            if cnt == "":
                cnt = ".2"
            else:
                cnt = cnt.lstrip(".")
                cnt = int(cnt) + 1
                cnt = str(cnt)
                cnt = "." + cnt
            return cnt

        def get_link_name(file, counter=""):
            max_num = 0
            for item in episodes_list:
                if item.episode_number > max_num:
                    max_num = item.episodeNumber
            max_num = len(str(max_num))

            link_name = title_name + " - s" + season_number + "e" + (
                str(file.number)).zfill(max_num) + counter + "." + file.getSuffix()
            return link_name

        for episode in episodes_list:
            episode.video_file.linkFileName = get_link_name(episode.video_file)
            episode.imageFile.linkFileName = get_link_name(episode.image_file)
            counter = ""
            for item in episode.audioFiles:
                item.linkFileName = get_link_name(item)
                counter = increment_counter(counter)
            counter = ""
            for item in episode.subsFiles:
                # print(counter)
                item.linkFileName = get_link_name(item)
                counter = increment_counter(counter)

    def checkTarget(self, targetPath, titleName, seasonNumber):
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

    def createLinks(self, episodes_list):
        season_number = self.season_number
        title_name = self.title_name
        target_path = self.target_path
        mount_point = self.mount_point
        true_mount_point = self.true_mount_point

        if not self.configuration.isIncludes("wrongOSNames", classFileOperations.FileOperations.osName()):
            self.prepare_files(episodes_list, title_name, season_number)
            self.checkTarget(target_path, title_name, season_number)
            targetFolder = classFileOperations.FileOperations.join(
                classFileOperations.FileOperations.join(target_path, title_name), "Season " + season_number)
            for episode in episodes_list:
                classFileOperations.FileOperations.symlink(classFileOperations.FileOperations.join(
                    episode.video_file.path.replace(mount_point, true_mount_point),
                    episode.video_file.fileName)
                    , classFileOperations.FileOperations.join(targetFolder, episode.video_file.linkFileName))
                classFileOperations.FileOperations.symlink(classFileOperations.FileOperations.join(
                    episode.imageFile.path.replace(mount_point, true_mount_point),
                    episode.imageFile.fileName)
                    , classFileOperations.FileOperations.join(targetFolder, episode.imageFile.linkFileName))
                for item in episode.subsFiles:
                    classFileOperations.FileOperations.symlink(classFileOperations.FileOperations.join(
                        item.path.replace(mount_point, true_mount_point),
                        item.fileName)
                        , classFileOperations.FileOperations.join(targetFolder, item.linkFileName))
                for item in episode.audioFiles:
                    classFileOperations.FileOperations.symlink(classFileOperations.FileOperations.join(
                        item.path.replace(mount_point, true_mount_point),
                        item.fileName)
                        , classFileOperations.FileOperations.join(targetFolder, item.linkFileName))
