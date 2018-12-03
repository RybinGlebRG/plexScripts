def check(episodesList):
    result = None
    #print(len(episodesList))
    for episode in episodesList:
        result = True
        for i in range(1, 6):

            if episode.episodeNumber == i:

                if episode.videoFile.fileName != "some episode"+str(i)+".mkv":
                    #result = False
                    return False
                for audioFile in episode.audioFiles:
                    if audioFile.fileName != "some episode"+str(i)+".ac3":
                        #result = False
                        return False
                for subsFile in episode.subsFiles:
                    if subsFile.fileName != "some episode"+str(i)+".ass":
                        #result = False
                        return False
    if result is None:
        return False
    else:
        return True
