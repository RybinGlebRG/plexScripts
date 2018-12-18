from seriesRoutine.Episodes import classEpisode


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

    def __iter__(self):
        return iter(self.episodes_list)

    def add(self, episode):
        self.episodes_list.append(episode)

    def load(self, video_files, subs_files, audio_files, image_files):
        for video_file in video_files:
            episode = classEpisode.Episode(video_file.number)
            episode.add_video_file(video_file)
            for subs_file in subs_files.filter_by_number(episode.episode_number):
                episode.add_subs_file(subs_file)
            for audio_file in audio_files.filter_by_number(episode.episode_number):
                episode.add_audio_file(audio_file)
            for image_file in image_files:
                image_file_copy = image_file.copy()
                image_file_copy.number = episode.episode_number
                episode.add_image_file(image_file_copy)
                break
            self.episodes_list.append(episode)

    def log(self):
        lines = []
        self.episodes_list.sort(key=lambda item: item.episode_number)
        lines.append("Файлы, сгруппированные по сериям:")
        for episode in self.episodes_list:
            lines.append("------------------------------------")
            lines.append(str(episode.episode_number) + ":")
            for video_file in episode.video_files:
                lines.append("Video: "+video_file.fileName)
            for audioFile in episode.audio_files:
                lines.append("Audio: "+audioFile.fileName)
            for subsFile in episode.subs_files:
                lines.append("Subtitle: "+subsFile.fileName)
            for image_file in episode.image_files:
                lines.append("Image: "+image_file.fileName)
        return lines
