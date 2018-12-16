import classFileOperations


class Link:

    def __init__(self, configuration):
        self.configuration = configuration
        self.season_number = self.configuration.getValue("seasonNumber")[0]
        self.title_name = self.configuration.getValue("titleName")[0]
        self.target_path = self.configuration.getValue("targetPath")[0]
        self.mount_point = self.configuration.getValue("mountPoint")[0]
        self.true_mount_point = self.configuration.getValue("trueMountPoint")[0]

    def prepare_files(self, episodes_list, title_name, season_number, target_path, mount_point, true_mount_point):
        def increment_counter(cnt):
            if cnt == "":
                cnt = ".2"
            else:
                cnt = cnt.lstrip(".")
                cnt = int(cnt) + 1
                cnt = str(cnt)
                cnt = "." + cnt
            return cnt

        def get_link_target(file, counter=""):
            max_num = 0
            for item in episodes_list:
                if item.episode_number > max_num:
                    max_num = item.episode_number
            max_num = len(str(max_num))

            link_name = title_name + " - s" + season_number + "e" + (
                str(file.number)).zfill(max_num) + counter + "." + file.getSuffix()
            # link_name = classFileOperations.FileOperations.join(target_path, link_name)
            targetFolder = classFileOperations.FileOperations.join(
                classFileOperations.FileOperations.join(target_path, title_name), "Season " + season_number)
            link_name = classFileOperations.FileOperations.join(targetFolder, link_name)
            file.link_target = link_name

        def get_link_source(file, mount_point, true_mount_point):
            true_mount_path = file.path.replace(mount_point, true_mount_point)
            link_name = classFileOperations.FileOperations.join(true_mount_path, file.fileName)
            file.link_source = link_name

        for episode in episodes_list:
            counter = ""
            for video_file in episode.video_files:
                get_link_target(video_file, counter)
                get_link_source(video_file, mount_point, true_mount_point)
                counter = increment_counter(counter)

            counter = ""
            for image_file in episode.image_files:
                get_link_target(image_file, counter)
                get_link_source(image_file, mount_point, true_mount_point)
                counter = increment_counter(counter)

            counter = ""
            for audio_file in episode.audio_files:
                get_link_target(audio_file, counter)
                get_link_source(audio_file, mount_point, true_mount_point)
                counter = increment_counter(counter)

            counter = ""
            for subs_file in episode.subs_files:
                get_link_target(subs_file, counter)
                get_link_source(subs_file, mount_point, true_mount_point)
                counter = increment_counter(counter)

    def check_target(self, targetPath, titleName, seasonNumber):
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
        self.prepare_files(episodes_list, title_name, season_number, target_path, mount_point, true_mount_point)

        if not self.configuration.isIncludes("wrongOSNames", classFileOperations.FileOperations.osName()):
            self.check_target(target_path, title_name, season_number)
            for episode in episodes_list:
                for video_file in episode.video_files:
                    classFileOperations.FileOperations.symlink(video_file.link_source, video_file.link_target)
                for image_file in episode.image_files:
                    classFileOperations.FileOperations.symlink(image_file.link_source, image_file.link_target)
                for subs_file in episode.subs_files:
                    classFileOperations.FileOperations.symlink(subs_file.link_source, subs_file.link_target)
                for audio_file in episode.audio_files:
                    classFileOperations.FileOperations.symlink(audio_file.link_source, audio_file.link_target)
