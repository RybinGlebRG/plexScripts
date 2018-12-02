from tests.testData.case_1 import case_1
from seriesRoutine import classFactory, classSeriesAnalyzer, classEpisode
import sys


# case_1.run()

def check(episodes_list, model_list):
    episodes_list.sort(key=lambda item: item.episodeNumber)
    model_list.sort(key=lambda item: item.episodeNumber)
    if len(episodes_list) != len(model_list):
        return False

    for i in range(0, len(episodes_list)):
        if not classEpisode.Episode.are_equal(episodes_list[i], model_list[i]):
            return False
    return True


configuration = classFactory.Factory.createConfiguration(sys.argv[1])

directoryPath = configuration.getValue("directoryPath")

filesList = classFactory.Factory.createFilesList(directoryPath, configuration)

videoFiles = filesList.filterVideoFiles()
audioFiles = filesList.filterAudioFiles()
subsFiles = filesList.filterSubsFiles()
imageFiles = filesList.filterImageFiles()

classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(videoFiles.get_list())
classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(subsFiles.get_list())
classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(audioFiles.get_list())

episodesList = classFactory.Factory.createEpisodesList(videoFiles.get_list(), subsFiles.get_list(),
                                                       audioFiles.get_list(), imageFiles.get_list()[0],
                                                       configuration)
result = check(episodesList, case_1.get_model_list())
print(result)
