# from seriesRoutine.Analyzer import classSeriesAnalyzer, unit_test
from seriesRoutine.Analyzer import ClassSeriesAnalyzerTests
from seriesRoutine.Episodes import ClassEpisodesListTests


# case_1.run()


def run():
    result = True

    analyzer_tests = ClassSeriesAnalyzerTests.AnalyzerTests()
    result = result and analyzer_tests.run()

    episodes_tests = ClassEpisodesListTests.EpisodesTests()
    result = result and episodes_tests.run()
    print(result)


#     configuration = classConfiguration.Configuration()
#     configuration.load(sys.argv[1])
#     if configuration is None:
#         return None
#     directory_path = None
#     for value in configuration.getValue("directoryPath"):
#         directory_path = value
#         break
#     log_path = directory_path
#     filesList = classFilesList.FilesList()
#     filesList.load(directory_path, configuration)
#
#     video_files = filesList.filter_by_suffixes(configuration.getValue("videoFileSuffixes"))
#     audio_files = filesList.filter_by_suffixes(configuration.getValue("audioFileSuffixes"))
#     subs_files = filesList.filter_by_suffixes(configuration.getValue("subsFileSuffixes"))
#     image_files = filesList.filter_by_suffixes(configuration.getValue("imageFileSuffixes"))
#
#     classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(video_files)
#     classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(subs_files)
#     classSeriesAnalyzer.SeriesAnalyzer.setFileNumber(audio_files)
#
#     episodes_list = ClassEpisodesList.EpisodesList()
#     episodes_list.load(video_files, subs_files, audio_files, image_files)
#     result = episodes_list == case_1.get_model_list()
#     print(result)
#
#
# case_1.prepare_conf()
# run()
#
# case_2.prepare_conf()
# run()
#
# case_3.prepare_conf()
# run()
run()
