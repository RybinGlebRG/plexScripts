# from seriesRoutine.Analyzer import classSeriesAnalyzer, unit_test
from seriesRoutine.Analyzer import ClassSeriesAnalyzerTests
from seriesRoutine.Episodes import ClassEpisodesListTests
from seriesRoutine.Files import ClassFilesListTests


# case_1.run()


def run():
    result = True

    analyzer_tests = ClassSeriesAnalyzerTests.AnalyzerTests()
    result = result and analyzer_tests.run()

    episodes_tests = ClassEpisodesListTests.EpisodesTests()
    result = result and episodes_tests.run()

    print("Overall:" + str(result))

run()
