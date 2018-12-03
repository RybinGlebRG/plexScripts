import classLogger


class EpisodesList:

    def __init__(self):
        self.episodes_list = []

    def log(self, directory):
        logger = classLogger.Logger()
        self.episodes_list.sort(key=lambda item: item.episodeNumber)
        logger.writeLog(directory, "info", "Файлы, сгруппированные по сериям:", "w+")
        for episode in self.episodes_list:
            logger.writeLog(directory, "info", "------------------------------------")
            logger.writeLog(directory, "info", str(episode.episodeNumber) + ":")
            logger.writeLog(directory, "info", episode.videoFile.fileName)
            for audioFile in episode.audioFiles:
                logger.writeLog(directory, "info", audioFile.fileName)
            for subsFile in episode.subsFiles:
                logger.writeLog(directory, "info", subsFile.fileName)
