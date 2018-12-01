def check(episodesList):
    result = True
    for episode in episodesList:
        for i in range(1, 6):
            if episode.episodeNumber == i:
                if episode.videoFile.fileName != "some episode1.mkv":
                    result = False
                for audioFile in episode.audioFiles:
                    if audioFile.fileName != "some episode1.ac3":
                        result = False
                for subsFile in episode.subsFiles:
                    if subsFile.fileName != "some episode1.ass":
                        result = False
    return result
