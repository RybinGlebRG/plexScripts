from seriesRoutine import classEpisode

import classLogger


class EpisodesList:

    def __init__(self):
        self.episodes_list = []

    def __eq__(self, other):
        if self.episodes_list != other.episodes_list:
            return False
        return True

    def __ne__(self, other):
        if self.episodes_list != other.episodes_list:
            return True
        return False

    def __getitem__(self, key):
        return self.episodes_list[key]


    def add(self, episode):
        self.episodes_list.append(episode)

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
