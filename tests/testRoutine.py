from tests.testData.case_1 import case_1
from tests.testData.case_2 import case_2
from tests.testData.case_3 import case_3
from seriesRoutine import classFactory, classSeriesAnalyzer, classEpisode
import sys


# case_1.run()

def run():
    configuration = classFactory.Factory.createConfiguration(sys.argv[1])

    directoryPath = configuration.getValue("directoryPath")
    filesList = classFactory.Factory.createFilesList(directoryPath, configuration)

    video_files = filesList.filterVideoFiles()
    audio_files = filesList.filterAudioFiles()
    subs_files = filesList.filterSubsFiles()
    image_files = filesList.filterImageFiles()

    classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(video_files)
    classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(subs_files)
    classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(audio_files)

    episodes_list = classFactory.Factory.createEpisodesList(video_files, subs_files,
                                                            audio_files, image_files,
                                                            configuration)
    result = episodes_list == case_1.get_model_list()
    print(result)


case_1.prepare_conf()
run()

case_2.prepare_conf()
run()

case_3.prepare_conf()
run()
